# to keep everything in organise

import dataclasses
from typing import TYPE_CHECKING
from . import models

if TYPE_CHECKING:
    from .models import User

@dataclasses.dataclass
class UserDataClass:
    email: str
    first_name: str
    last_name: str

    # id and password must be last, because have value
    password: str = None
    id: int = None #because Ids only created upon creation

    @classmethod
    def from_instance(cls, user: "User") -> "UserDataClass":
        return cls(
            first_name= user.first_name,
            last_name = user.last_name,
            email= user.email,
            id=user.id
        )

def create_user(user_dc: "UserDataClass") -> "UserDataClass": # user_dc - user Data Class
    instance = models.User(
        first_name = user_dc.first_name,
        last_name = user_dc.last_name,
        email= user_dc.email
    )

    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()
    return UserDataClass.from_instance(instance)
