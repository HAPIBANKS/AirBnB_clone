#!/usr/bin/python3
"""
class module review
"""


from models.base_model import BaseModel


class Review:
    """
    Public class attributes:
    place_id: string - empty: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
