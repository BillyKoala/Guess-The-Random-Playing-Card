"""
Author: Billy Knight - March 2022.

Project Name: Guess The Random Playing Card.

This is the classes.py file created to reference
the one single user-defined class in this project.
"""

import globals
from constants import *

class RandomPlayingCard:

    # This class will be used to record all the properties of the randomly selected playing card.

    def __init__(self,
                 card_id, card_number, card_suit,
                 suit_name, suit_colour,
                 picture_name, card_image_path):

        self.card_id = card_id
        self.card_number = card_number
        self.card_suit = card_suit
        self.suit_name = suit_name
        self.suit_colour = suit_colour
        self.picture_name = picture_name
        self.card_image_path = card_image_path
        self.joker_image_path = joker_image_path
        self.joker_jack_image_path = joker_jack_image_path
        self.card_suits_image_path =card_suits_image_path
        self.developer_mugshot = developer_mugshot
        self.developer_mugshot_inv = developer_mugshot_inv

        def get_card_id(self):
            return self.card_id

        def set_card_id(self, card_id):
            self.card_number = card_id

        def get_card_number(self):
            return self.card_number

        def set_card_number(self, card_number):
            self.card_number = card_number

        def get_card_suit(self):
            return self.card_suit

        def set_card_suit(self, card_suit):
            self.card_suit = card_suit

        def get_suit_name(self):
            return self.suit_name

        def set_suit_name(self, suit_name):
            self.suit_name = suit_name

        def get_picture_name(self):
            return self.picture_name

        def set_picture_name(self, picture_name):
            self.picture_name = picture_name

        def get_card_image_path(self):
            return self.card_image_path

        def set_card_image_path(self, image_path):
               self.card_image_path = card_image_path

    # STATIC VARIABLES
        def get_suit_colour(self):
            return self.suit_colour

        def get_joker_image_path(self):
            return self.joker_image_path

        def get_card_suits_image_path(self):
            return self.card_suits_image_path_path

        def get_developer_mugshot(self):
            return self.developer_mugshot

        def get_developer_mugshot_inv(self):
            return self.developer_mugshot_inv
