from flask import render_template, request, Blueprint
from .bus_service import BusService

bus_service = BusService()

bp = Blueprint('bus', __name__, url_prefix='/bus')

@bp.route("/main")
def bus_main():
    trans = bus_service.trans_list()

    return render_template("bus_main.html", trans=trans)
