import datetime

"""
A class to store an Event and its information.
"""
class Event:

    """
    An event with a type (homework, assignment) and an dict of time slots
    with the key being the Day, and the value being an array time slots.
    >>> test_deadline = datetime.datetime(2019, 1, 21, 14, 30) # date is year, month, day, hour, minute
    >>> Adrian_event = Event("Assignment", test_deadline, 4.5)
    """
    def __init__(self, _type, deadline, duration):
        self.type = _type
        self.time_slots = {}
        self.deadline = deadline
        self.duration = duration

