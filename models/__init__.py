from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .visitor import VisitorModel
from .location import LocationModel
from .dateTime import DateTimeModel
from .feedback import FeedbackModel
from .moderator import ModeratorModel
from .hotel import HotelModel