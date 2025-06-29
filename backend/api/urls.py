from api import views as api_views
from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [

    # Authentication Endpoints

    path("user/token/", api_views.MyTokenObtainPairView.as_view()), # pass it sa view method
    # http://127.0.0.1:8000/api/v1/user/token/ - try to login with existing acount to get token
    # go to jwtio pass the token
    # token as membership card - check for user info
    path("user/token/refresh/", TokenRefreshView.as_view()), #  get refresh token from http://127.0.0.1:8000/api/v1/user/token/  and pass it  http://127.0.0.1:8000/api/v1/user/token/refresh/
    path("user/register/", api_views.RegisterView.as_view()), # http://127.0.0.1:8000/api/v1/user/register/
    path("user/password-reset/<email>/", api_views.PasswordResetEmailVerifyAPIView.as_view()),
    path("user/password-change/", api_views.PasswordChangeAPIView.as_view()),

    # core endpoints
    path("course/category/", api_views.CategoryListAPIView.as_view()),
    path("course/course-list/", api_views.CourseListAPIView.as_view()),
    path("course/search/", api_views.SearchCourseAPIView.as_view()),
    path("course/course-detail/<slug>/", api_views.CourseDetailAPIView.as_view()),
    path("course/cart/", api_views.CartAPIView.as_view()),
    path("course/cart-list/<cart_id>/", api_views.CartListAPIView.as_view()),
    path("course/cart-item-delete/<cart_id>/<item_id>/", api_views.CartItemDeleteAPIView.as_view()),
    path("cart/stats/<cart_id>/", api_views.CartStatsAPIView.as_view()),
    path("order/create-order/", api_views.CreateOrderAPIView.as_view()),
    path("order/checkout/<oid>/", api_views.CheckoutAPIView.as_view()),
    path("order/coupon/", api_views.CouponApplyAPIView.as_view()),
    path("payment/stripe-checkout/<order_oid>/", api_views.StripeCheckoutAPIView.as_view()),
    path("payment/payment-sucess/", api_views.PaymentSuccessAPIView.as_view()),



     # Student API Endpoints





      # Teacher Routes
   

]