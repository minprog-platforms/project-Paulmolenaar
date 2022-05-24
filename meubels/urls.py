from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("overons", views.over_ons, name="overons"),
    path("product/<str:product>", views.product, name="product"),
    path("kamerinrichten", views.kamer_inrichten, name="kamer_inrichten"),
    path("bestellen", views.bestellen, name="bestellen"),
    path("afgerond", views.afgerond, name="afgerond"),
    path("winkelwagen", views.winkelwagen, name="winkelwagen"),
    # path("categories", views.category, name="category"),
    # path("categories/<str:categoryName>", views.category_listings, name="category_listing"),  
    # path("newlist", views.new_list, name="new_list"),
    # path("listing/<str:listing>", views.listing, name="listing"),
    # path("listing_closed/<str:listing>", views.listing_closed, name="listing_closed"),
    # path("watchlist", views.watchlist, name="watchlist"),   
]

