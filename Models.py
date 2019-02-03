import collections
from Events import Event
from _datetime import datetime

EPSILON = 0.005


class Calendar:
    def __init__(self):
        self.week1 = Week()
        self.week2 = Week()
        self.week3 = Week()
        self.week4 = Week()
        self.week5 = Week()


class Week:

    def __init_(self):
        self.Monday = Day("Monday")
        self.Tuesday = Day("Tuesday")
        self.Wednesday = Day("Wednesday")
        self.Thursday = Day("Thursday")
        self.Friday = Day("Friday")
        self.Saturday = Day("Saturday")
        self.Sunday = Day("Sunday")
        self.test = "test"


class Day:

    def __init__(self, day):
        self.day = day
        self.time_slots = {1.0: [], 13.0: [], 1.5: [], 13.5: [], 2.0: [], 14.0: [], 2.5: [], 14.5: [],
                            3.0: [], 15.0: [], 3.5: [], 15.5: [], 4.0: [], 16.0: [], 4.5: [], 16.5: [],
                            5.0: [], 17.0: [], 5.5: [], 17.5: [], 6.0: [], 18.0: [], 6.5: [], 18.5: [],
                            7.0: [], 19.0: [], 7.5: [], 19.5: [], 8.0: [], 20.0: [], 8.5: [], 20.5: [],
                            9.0: [], 21.0: [], 9.5: [], 21.5: [], 10.0: [], 22.0: [], 10.5: [], 22.5: [],
                            11.0: [], 23.0: [], 11.5: [], 23.5: [], 12.0: [], 0.0: [], 12.5: [], 0.5: []}
        #self.time_slots = {'1:00': [], '13:00': [], '1:30': [], '13:30': [], '2:00': [], '14:00': [], '2:30': [], '14:30': [],
        #                    '3:00': [], '15:00': [], '3:30': [], '15:30': [], '4:00': [], '16:00': [], '4:30': [], '16:30': [],
        #                    '5:00': [], '17:00': [], '5:30': [], '17:30': [], '6:00': [], '18:00': [], '6:30': [], '18:30': [],
        #                    '7:00': [], '19:00': [], '7:30': [], '19:30': [], '8:00': [], '20:00': [], '8:30': [], '20:30': [],
        #                    '9:00': [], '21:00': [], '9:30': [], '21:30': [], '10:00': [], '22:00': [], '10:30': [], '22:30': [],
        #                    '11:00': [], '23:00': [], '11:30': [], '23:30': [], '12:00': [], '00:00': [], '12:30': [], '00:30': []}

    # input: time of day
    # returns list of items (event types) that are most to least frequent during that time; removes duplicates
    def commonEvents (self, time):
        timeArray = self.time_slots[time]
        counts = collections.Counter(timeArray)

        sortedEvents = []
        for k in sorted(counts, key=counts.__getitem__, reverse=True):
            sortedEvents.extend([k for _ in range(counts[k])])

        sortedEvents_new = []
        for item in sortedEvents:
            if item not in sortedEvents_new:
                sortedEvents_new.append(item)

        return sortedEvents_new

    # input: event type
    # output: returns list of time lists that are most common for the event type
    def commonTime (self, eventType):
        bestTimes = []

        for timeList in self.time_slots :
            if eventType == (self.time_slots[timeList][0]):
                if timeList not in bestTimes: bestTimes.append(timeList)

        return bestTimes

    # input: duration of event, and list of optimal times
    # output: returns list of times that cover the duration of event
    def timeBlock (self, duration, bestTimes):
        goodTimes = []
        timeUnits = duration / 30
        i = 0
        while (i < 48) : #loops through all times
            a = 0

            while (a < timeUnits and a < len(bestTimes)) :

                if i == bestTimes[a]:
                    goodTimes.append(i)
                a = a + 1

            i = i + 0.5
        return goodTimes


calendar = Calendar()

firstMeeting = Event("Meeting", datetime(2019, 1, 4, 15, 30), 30)
secondHomework = Event("Homework", datetime(2019, 1, 6, 12, 00), 60)
thirdHomework = Event("Homework", datetime(2019, 1, 8, 15, 30), 30)
fourthHomework = Event("Homework", datetime(2019, 1, 11, 15, 20), 30)
fifthHomework = Event("Homework", datetime(2019, 1, 13, 12, 00), 60)
sixthHomework = Event("Homework", datetime(2019, 1, 15, 15, 30), 30)

monday = Day('Monday')
tuesday = Day('Tuesday')
wednesday = Day('Wednesday')
thursday = Day('Thursday')
friday = Day('Friday')
saturday = Day('Saturday')
sunday = Day("Sunday")



monday.time_slots = {1.0: ["Meeting", "Studying", "Homework", "Meeting","Homework", "Homework"], 13.5: ["Studying", "Studying", "Stuyding", "Projects", "Errands"]}
tuesday.time_slots = {12.0: ["Meeting", "Errands", "Errands", "Errands", "Errands", "Meeting"], 13.5: ["TestPrep", "TestPrep", "TestPrep", "Projects", "Errands"]}
wednesday.time_slots = {1.0: ["Meeting", "Meeting", "Meeting", "Meeting","Homework", "Homework"], 13.5: ["Studying", "Studying", "Stuyding", "Projects", "Errands"]}
thursday.time_slots = {1.0: ["Meeting", "Studying", "Homework", "Meeting","Homework", "Homework"], 13.5: ["Studying", "Studying", "Stuyding", "Projects", "Errands"]}
friday.time_slots = {1.0: ["Meeting", "Studying", "Homework", "Meeting","Homework", "Homework"], 13.5: ["Studying", "Studying", "Stuyding", "Projects", "Errands"]}

days = [monday,tuesday,wednesday,thursday,friday]

for daysingular in days:
    print(daysingular.timeBlock(firstMeeting.duration, daysingular.commonTime("Meeting")))




