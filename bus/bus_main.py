from flask import render_template, request, Blueprint
from .bus_service import BusService , LowBusService

bus_service = BusService()
low_service = LowBusService()

bp = Blueprint('bus', __name__, url_prefix='/bus')

@bp.route("/main")
def bus_main():
    trans = bus_service.trans_list()

    return render_template("bus_main.html", trans=trans)

@bp.route('/station')
def low_bus():
    station = request.args.get('station')
    low_list = low_service.getBusStopName()
    res = low_service.low_bus_list()
    return render_template('bus_low.html', low=low_list, station=station , res=res)

@bp.route('/station1')
def station_list():
    res = low_service.low_bus_list()
    return render_template('station.html',res=res)

