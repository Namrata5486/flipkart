from django.urls import path
from . import views
from app.views import ProductRegister,ProductList,ProductUpdate,ProductDelete

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("userlogout/", views.userlogout, name="userlogout"),
    path("fashionlist/", views.fashionlist, name="fashionlist"),
    path("shoeslist/", views.shoeslist, name="shoeslist"),
    path("mobilelist/", views.mobilelist, name="mobilelist"),
    path("electronicslist/", views.electronicslist, name="electronicslist"),
    path("clothlist/", views.clothlist, name="clothlist"),
    path("grocerylist/", views.grocerylist, name="grocerylist"),
    path("searchproduct/", views.searchproduct, name="searchproduct"),
    path(
        "request_password_reset/",
        views.request_password_reset,
        name="request_password_reset",
    ),
    path("reset_password/<username>/", views.reset_password, name="reset_password"),
    path("showpricerange/", views.showpricerange, name="showpricerange"),
    path("sortingbyprice/", views.sortingbyprice, name="sortingbyprice"),
    path("showcarts/", views.showcarts, name="showcarts"),
    path("addtocart/<int:productid>",views.addtocart,name="addtocart"),
    path("removecart/<int:productid>",views.removecart,name="removercart"),
    path("updateqty/<int:productid>",views.updateqty,name="updateqty"),
    path("addaddress/", views.addaddress,name="addaddress"),
    path("showaddress/",views.showaddress,name="showaddress"),
    path("ProductRegister/", ProductRegister.as_view(), name="ProductRegister"),
    path("ProductList/", ProductList.as_view(), name="ProductList"),
    path("ProductUpdate/<int:pk>", ProductUpdate.as_view(), name="ProductUpdate"),
    path("ProductDelete/<int:pk>", ProductDelete.as_view(), name="ProductDelete"),
]

