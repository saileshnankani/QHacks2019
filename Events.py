"""
A class to store an Event and its information.
"""
class Event:

    """
    An event with a type (homework, assignment) and an dict of time slots
    with the key being the Day, and the value being an array time slots.
    """
    def __init__(self, type, time_slots):
        self.type = type
        self.time_slots = time_slots



