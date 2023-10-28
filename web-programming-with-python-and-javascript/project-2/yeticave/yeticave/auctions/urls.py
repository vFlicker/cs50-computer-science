from django.urls import path

from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("listing/<int:listing_id>/", views.ListingView.as_view(), name="listing"),
    path("listing/<int:listing_id>/toggle_watchlist/", views.toggle_watchlist, name="toggle_watchlist"),
    path("listing/<int:listing_id>/close_bid/", views.close_bid, name="close_bid"),
    path("create_listing/", views.create_listing, name="create_listing"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("categories/<int:category_id>/", views.categories, name="categories"),
]
