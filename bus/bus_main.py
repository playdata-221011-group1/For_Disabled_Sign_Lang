from flask import render_template, request, Blueprint
from .bus_service import BusService , LowBusService

bus_service = BusService()
low_service = LowBusService()

bp = Blueprint('bus', __name__, url_prefix='/bus')

@bp.route("/main")
def bus_main():
    bus_list = bus_service.bus_list()

    return render_template("bus_main.html", bus_list=bus_list)


@bp.route('/low')
def low_bus():
    low_list = low_service.getBusStopName()
    return render_template('bus_low.html', low=low_list)