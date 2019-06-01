from flask import  Blueprint

lost_and_found = Blueprint('lost_and_found',
                           __name__,
                           template_folder='templates',
                           static_folder='static',
                           url_prefix='/LostAndFound')

from . import views

