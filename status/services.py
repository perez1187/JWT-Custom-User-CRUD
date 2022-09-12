import dataclasses
import datetime

from . import models as status_models

from user import services as user_services

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Status

@dataclasses.dataclass
class StatusDataClass:
    content: str

    # this 3 we do not post (?)
    date_published: datetime.datetime = None
    user: user_services.UserDataClass = None
    id: int = None

    @classmethod
    def from_instance(cls, status_model:"Status") -> "StatusDataClass": # to map our user class
        return cls(
            content = status_model.content,
            date_published = status_model.date_published,
            id = status_model.id,
            user = status_model.user

        )
# we can do it without jego podmiany danych? potestowac
def create_status(user, status:"StatusDataClass") -> "StatusDataClass":
    status_create = status_models.Status.objects.create(
        content=status.content,
        user=user
    )

    return StatusDataClass.from_instance(status_model=status_create)