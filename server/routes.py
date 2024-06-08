# server/routes.py
from flask import Blueprint
from flask_restful import Api
from resources import (
    UserRegistration,
    UserLogin,
    OrderResource,
    OrderItemResource,
    MenuItemResource,
    ReservationResource,
)

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(UserRegistration, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(OrderResource, "/orders", "/orders/<int:order_id>")
api.add_resource(
    OrderItemResource,
    "/orders/<int:order_id>/items",
    "/orders/<int:order_id>/items/<int:order_item_id>",
)
api.add_resource(MenuItemResource, "/menu_items", "/menu_items/<int:menu_item_id>")
api.add_resource(
    ReservationResource,
    "/reservations",
)
