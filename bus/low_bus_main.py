from flask import render_template, request, Blueprint
from .low_bus_service import LowBusService

low_bus_service = LowBusService()

bp = Blueprint('low_bus', __name__, url_prefix='/bus')


@bp.route("/low_main")
def low_bus_main():
    #low_bus_list = low_bus_service.html
    low_bus_list = low_bus_service.low_bus_list()

    return render_template("low_bus_main.html", ll=low_bus_list)
