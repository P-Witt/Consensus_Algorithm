import numpy as np
import hashlib as h
import matplotlib.pyplot as plt

"""
The idea of this program is to recreate the basic workings of the bitcoin protocol to ensure a decentralised value
"""


def generate_public_key(safe_key):
    pass


def validate_transaction(block, depth):
    pass


def create_new_block(previous_block, hash_zeroes_needed):
    pass


class agent:
    def __init__(self, safe_key, public_key):
        self.safe_key = safe_key
        self.public_key = public_key

    def sign_transaction(self, message):
        pass
