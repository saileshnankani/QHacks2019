from _datetime import datetime
from Events import Event
from Models import Week
from Models import Day


class Calendar:
    def __init__(self):
        self.week1 = Week()
        self.week2 = Week()
        self.week3 = Week()
        self.week4 = Week()
        self.week5 = Week()

# -- pre-populated data --


calendar = Calendar()

firstHomework = Event("Homework", datetime(2019, 1, 4, 15, 30), 30)
secondHomework = Event("Homework", datetime(2019, 1, 6, 12, 00), 60)
thirdHomework = Event("Homework", datetime(2019, 1, 8, 15, 30), 30)
fourthHomework = Event("Homework", datetime(2019, 1, 11, 15, 20), 30)
fifthHomework = Event("Homework", datetime(2019, 1, 13, 12, 00), 60)
sixthHomework = Event("Homework", datetime(2019, 1, 15, 15, 30), 30)

calendar.week1.test
calendar.week1.Friday.time_slots.append(firstHomework)
calendar.week2.Sunday.time_slots.append(secondHomework)
calendar.week2.Tuesday.time_slots.append(thirdHomework)
calendar.week2.Friday.time_slots.append(fourthHomework)
calendar.week3.Sunday.time_slots.append(fifthHomework)
calendar.week3.Tuesday.time_slots.append(sixthHomework)

firstTestPrep = Event("TestPrep", datetime(2019, 1, 5, 19, 00), 30)
secondTestPrep = Event("TestPrep", datetime(2019, 1, 7, 14, 30), 60)
thirdTestPrep = Event("TestPrep", datetime(2019, 1, 4, 19, 00), 30)
fourthTestPrep = Event("TestPrep", datetime(2019, 1, 6, 14, 30), 60)
fifthTestPrep = Event("TestPrep", datetime(2019, 1, 8, 15, 30), 30)

calendar.week1.Friday.time_slots.append(firstTestPrep)
calendar.week1.Saturday.time_slots.append(secondTestPrep)
calendar.week2.Sunday.time_slots.append(thirdTestPrep)
calendar.week2.Monday.time_slots.append(fourthTestPrep)
calendar.week2.Tuesday.time_slots.append(fifthTestPrep)

firstErrand = Event("Errands", datetime(2019, 1, 9, 17, 00), 30)
secondErrand = Event("Errands", datetime(2019, 1, 10, 17, 00), 30)
thirdErrand = Event("Errands", datetime(2019, 1, 11, 17, 00), 30)
fourthErrand = Event("Errands", datetime(2019, 1, 12, 17, 00), 30)

calendar.week2.Wednesday.time_slots.Tuesday.append(firstErrand)
calendar.week2.Thursday.time_slots.append(secondErrand)
calendar.week2.Friday.time_slots.append(thirdErrand)
calendar.week2.Saturday.time_slots.append(fourthErrand)

firstProject = Event("Projects", datetime(2019, 1, 6, 17, 00), 90)
secondProject = Event("Projects", datetime(2019, 1, 7, 11, 00), 180)
thirdProject = Event("Projects", datetime(2019, 1, 8, 17, 00), 90)
fourthProject = Event("Projects", datetime(2019, 1, 9, 11, 00), 180)
fifthProject = Event("Projects", datetime(2019, 1, 10, 17, 00), 90)
sixthProject = Event("Projects", datetime(2019, 1, 11, 11, 00), 180)

calendar.week2.Sunday.time_slots.append(firstHomework)
calendar.week2.Monday.time_slots.append(secondHomework)
calendar.week2.Tuesday.time_slots.append(thirdHomework)
calendar.week2.Wednesday.time_slots.append(fourthHomework)
calendar.week2.Thursday.time_slots.append(fifthHomework)
calendar.week2.Friday.time_slots.append(sixthHomework)

firstStudying = Event("Studying", datetime(2019, 1, 6, 17, 00), 90)
secondStudying = Event("Studying", datetime(2019, 1, 7, 11, 00), 30)
thirdStudying = Event("Studying", datetime(2019, 1, 8, 17, 00), 90)
fourthStudying = Event("Studying", datetime(2019, 1, 9, 11, 00), 30)
fifthStudying = Event("Studying", datetime(2019, 1, 10, 17, 00), 90)
sixthStudying = Event("Studying", datetime(2019, 1, 11, 11, 00), 30)

calendar.week2.Sunday.time_slots.append(firstStudying)
calendar.week2.Monday.time_slots.append(secondStudying)
calendar.week2.Tuesday.time_slots.append(thirdStudying)
calendar.week2.Wednesday.time_slots.append(fourthStudying)
calendar.week2.Thursday.time_slots.append(fifthStudying)
calendar.week2.Friday.time_slots.append(sixthStudying)

# -- end of pre-populated data --

day = Day('Monday')
day.time_slots = {1.0: ["Homework", "Homework", "Meeting", "Studying", "Homework", "Meeting"]}
day.commonEvents(1.0)



