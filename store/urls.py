from rest_framework_nested import routers

from store.views import (
    AddressViewSet,
    CartItemViewSet,
    CartViewSet,
    CollectionViewSet,
    CustomerViewSet,
    OrderItemViewSet,
    OrderViewSet,
    ProductViewSet,
    ProductImageViewSet,
)


router = routers.DefaultRouter()
# parent routers
router.register("collections", CollectionViewSet, basename="collections")
router.register("products", ProductViewSet, basename="products")
router.register("customers", CustomerViewSet, basename="customers")
router.register("orders", OrderViewSet, basename="orders")
router.register("carts", CartViewSet, basename="carts")

# Sub parent routers
order_router = routers.NestedDefaultRouter(router, "orders", lookup="order")
cart_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
customer_router = routers.NestedDefaultRouter(router, "customers", lookup="customer")
product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
# nested routers
order_router.register("items", OrderItemViewSet, basename="order_items")
cart_router.register("items", CartItemViewSet, basename="cart_items")
customer_router.register("addresses", AddressViewSet, basename="addresses")
product_router.register("images", ProductImageViewSet, basename="product_images")


urlpatterns = (
    router.urls
    + order_router.urls
    + cart_router.urls
    + customer_router.urls
    + product_router.urls
)
