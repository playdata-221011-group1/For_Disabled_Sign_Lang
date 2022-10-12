from flask import render_template, request, Blueprint
from bus_service import BusService

bus_service = BusService()

bp = Blueprint('bus', __name__, url_prefix='/bus')

@bp.route("/main")
def bus_main():
    bus_list = bus_service.bus_list()

    return render_template("bus_main.html", bus_list=bus_list)
