import factory
from app.models.event_copyright import db, EventCopyright
import app.factories.common as common
from app.factories.event import EventFactoryBasic


class EventCopyrightFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = EventCopyright
        sqlalchemy_session = db.session

    event = factory.RelatedFactory(EventFactoryBasic)
    holder = common.string_
    holder_url = common.url_
    licence = common.string_
    licence_url = common.url_
    year = 2007
    logo = common.url_
