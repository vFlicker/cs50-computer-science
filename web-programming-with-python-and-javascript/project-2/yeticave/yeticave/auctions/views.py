from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required
from django.views import View


from .forms import ListingForm, BidForm, CommentForm
from .models import Bid, Listing, Watchlist, Comment, Category


def index(request):
    # TODO: Має дозволити користувачам переглянути всі АКТИВНІ АУКЦІОНИ.

    # Check if the user is authenticated (logged in)
    if request.user.is_authenticated:
        # If the user is logged in, get a list of all products and add the in_watchlist flag for each product
        listings = Listing.objects.all().prefetch_related(
            Prefetch(
                'watchlist_set',
                queryset=Watchlist.objects.filter(user=request.user),
                to_attr='in_watchlist'
            )
        )
    else:
        # If the user is not logged in, simply get a list of all products without the in_watchlist flag
        listings = Listing.objects.all()

    return render(request, "auctions/index.html", {
        "listings": listings,
    })


class ListingView(View):
    # TODO: Додати сторінку мої ставки

    # TODO: Якщо користувач увійшов до облікового запису і він є автором аукціону, він повинен мати змогу «закрити» аукціон на цій сторінці, що зробить автора найбільшої ставки переможцем аукціону, а сам аукціон стане неактивним.

    # TODO: Якщо користувач увійшов до облікового запису на сторінці закритого аукціону і він є переможцем цього аукціону, він має отримати повідомлення про це.

    template_name = "auctions/listing.html"
    form_bid = BidForm
    form_comment = CommentForm

    def get(self, request, listing_id):
        listing = Listing.objects.get(pk=listing_id)
        bids = Bid.objects.filter(listing=listing).order_by("-bid_time")[:10]
        is_creator = request.user.is_authenticated and listing.creator == request.user
        listing.in_watchlist = request.user.watchlist.filter(item=listing)
        comments = Comment.objects.filter(
            listing=listing).order_by("-created_at")

        context = {
            "listing": listing,
            "form_bid": self.form_bid(),
            "form_comment": self.form_comment(),
            "is_creator": is_creator,
            "bids": bids,
            "comments": comments,
        }

        return render(request, "auctions/listing.html", context)

    def post(self, request, listing_id):
        listing = Listing.objects.get(pk=listing_id)
        bids = Bid.objects.filter(listing=listing).order_by("-bid_time")[:10]
        is_creator = request.user.is_authenticated and listing.creator == request.user
        form_type = request.POST.get("form_type")
        listing.in_watchlist = request.user.watchlist.filter(item=listing)
        comments = Comment.objects.filter(
            listing=listing).order_by("-created_at")

        if form_type == "comment" and not is_creator:
            form_comment = self.form_comment(request.POST)
            if form_comment.is_valid():
                comment = form_comment.save(commit=False)
                comment.listing = listing
                comment.user = request.user
                comment.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        elif form_type == "bid" and not is_creator:
            form_bid = self.form_bid(request.POST)
            if form_bid.is_valid():
                bid = form_bid.save(commit=False)
                bid.listing = listing
                bid.bidder = request.user
                if bid.bid_amount > listing.current_price:
                    bid.save()
                    listing.current_price = bid.bid_amount
                    listing.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    form_bid.add_error(
                        'bid_amount', 'Bid must be greater than the current price.')
        else:
            form_bid = self.form_bid()
            form_comment = self.form_comment()

        context = {
            "listing": listing,
            "form_bid": form_bid,
            "form_comment": form_comment,
            "is_creator": is_creator,
            "bids": bids,
            "comments": comments,
        }

        return render(request, "auctions/listing.html", context)


@login_required
def close_bid(listing_id):
    pass


def categories(request, category_id):
    listings = Listing.objects.filter(category=category_id)
    category = Category.objects.get(pk=category_id)

    return render(request, "auctions/categories.html", {
        "listings": listings,
        "category": category,
    })


def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.creator = request.user
            listing.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ListingForm()

    return render(request, "auctions/create_listing.html", {"form": form})


@login_required
def watchlist(request):
    # Get a list of all products that are in the tracking list for the current user
    listings = Listing.objects.filter(
        watchlist__user=request.user
    ).prefetch_related(
        Prefetch(
            'watchlist_set',
            queryset=Watchlist.objects.filter(user=request.user),
            to_attr='in_watchlist'
        )
    )

    return render(request, "auctions/watchlist.html", {
        "listings": listings,
    })


@login_required
def toggle_watchlist(request, listing_id):
    item = get_object_or_404(Listing, pk=listing_id)
    watchlist_item, created = Watchlist.objects.get_or_create(
        user=request.user, item=item)

    if not created:
        watchlist_item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))