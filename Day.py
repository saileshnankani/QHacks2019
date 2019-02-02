import collections

class Week:

    def __init_(self):
        self.Monday = Day("Monday")
        self.Tuesday = Day("Tuesday")
        self.Wednesday = Day("Wednesday")
        self.Thursday = Day("Thursday")
        self.Friday = Day("Friday")
        self.Saturday = Day("Saturday")
        self.Sunday = Day("Sunday")


class Day:

    def __init__(self, day):
        self.day = day
        self.time_slots = {'1:00': [], '13:00': [], '1:30': [], '13:30': [], '2:00': [], '14:00': [], '2:30': [], '14:30': [],
                           '3:00': [], '15:00': [], '3:30': [], '15:30': [], '4:00': [], '16:00': [], '4:30': [], '16:30': [],
                           '5:00': [], '17:00': [], '5:30': [], '17:30': [], '6:00': [], '18:00': [], '6:30': [], '18:30': [],
                           '7:00': [], '19:00': [], '7:30': [], '19:30': [], '8:00': [], '20:00': [], '8:30': [], '20:30': [],
                           '9:00': [], '21:00': [], '9:30': [], '21:30': [], '10:00': [], '22:00': [], '10:30': [], '22:30': [],
                           '11:00': [], '23:00': [], '11:30': [], '23:30': [], '12:00': [], '00:00': [], '12:30': [], '00:30': []}

    # input: time of day
    # returns list of items (event types) that are most to least frequent during that time; removes duplicates
    def common (self, time):
        a = self.time_slots[time]
        counts = collections.Counter(a)
        sortedEvents = []
        for k in sorted(counts, key=counts.__getitem__, reverse=True):
            sortedEvents.extend([k for _ in range(counts[k])])

        sortedEvents_new = []
        for item in sortedEvents:
            if item not in sortedEvents_new: sortedEvents_new.append(item)

        # print (sortedEvents_new)

