from _datetime import datetime
from Events import Event

calendar = []

# -- pre-populated data --

firstHomework = Event("Homework", datetime(2019, 1, 4, 15, 30), 30)
secondHomework = Event("Homework", datetime(2019, 1, 6, 12, 00), 60)
thirdHomework = Event("Homework", datetime(2019, 1, 8, 15, 30), 30)
fourthHomework = Event("Homework", datetime(2019, 1, 11, 15, 20), 30)
fifthHomework = Event("Homework", datetime(2019, 1, 13, 12, 00), 60)
sixthHomework = Event("Homework", datetime(2019, 1, 15, 15, 30), 30)

calendar.append(firstHomework)
calendar.append(secondHomework)
calendar.append(thirdHomework)
calendar.append(fourthHomework)
calendar.append(fifthHomework)
calendar.append(sixthHomework)

firstMeeting = Event("Meeting", datetime(2019, 1, 5, 9, 30), 30)
secondMeeting = Event("Meeting", datetime(2019, 1, 7, 16, 00), 90)
thirdMeeting = Event("Meeting", datetime(2019, 1, 12, 9, 30), 30)
fourthMeeting = Event("Meeting", datetime(2019, 1, 14, 16, 00), 90)
fifthMeeting = Event("Meeting", datetime(2019, 1, 19, 9, 30), 30)
sixthMeeting = Event("Meeting", datetime(2019, 1, 21, 16, 00), 90)

calendar.append(firstMeeting)
calendar.append(secondMeeting)
calendar.append(thirdMeeting)
calendar.append(fourthMeeting)
calendar.append(fifthMeeting)
calendar.append(sixthMeeting)

firstTestPrep = Event("TestPrep", datetime(2019, 1, 18, 19, 00), 30)
secondTestPrep = Event("TestPrep", datetime(2019, 1, 20, 14, 30), 60)
thirdTestPrep = Event("TestPrep", datetime(2019, 1, 22, 19, 00), 30)
fourthTestPrep = Event("TestPrep", datetime(2019, 1, 25, 14, 30), 60)
fifthTestPrep = Event("TestPrep", datetime(2019, 1, 27, 15, 30), 30)

calendar.append(firstTestPrep)
calendar.append(secondTestPrep)
calendar.append(thirdTestPrep)
calendar.append(fourthTestPrep)
calendar.append(fifthTestPrep)

firstErrand = Event("Errands", datetime(2019, 1, 19, 17, 00), 30)
secondErrand = Event("Errands", datetime(2019, 1, 21, 17, 00), 30)
thirdErrand = Event("Errands", datetime(2019, 1, 26, 17, 00), 30)
fourthErrand = Event("Errands", datetime(2019, 1, 28, 17, 00), 30)

calendar.append(firstErrand)
calendar.append(secondErrand)
calendar.append(thirdErrand)
calendar.append(fourthErrand)

firstProject = Event("Projects", datetime(2019, 1, 18, 17, 00), 90)
secondProject = Event("Projects", datetime(2019, 1, 20, 11, 00), 180)
thirdProject = Event("Projects", datetime(2019, 1, 26, 17, 00), 90)
fourthProject = Event("Projects", datetime(2019, 1, 28, 11, 00), 180)
fifthProject = Event("Projects", datetime(2019, 1, 15, 17, 00), 90)
sixthProject = Event("Projects", datetime(2019, 1, 13, 11, 00), 180)

calendar.append(firstHomework)
calendar.append(secondHomework)
calendar.append(thirdHomework)
calendar.append(fourthHomework)
calendar.append(fifthHomework)
calendar.append(sixthHomework)

firstStudying = Event("Studying", datetime(2019, 1, 19, 17, 00), 90)
secondStudying = Event("Studying", datetime(2019, 1, 21, 11, 00), 30)
thirdStudying = Event("Studying", datetime(2019, 1, 26, 17, 00), 90)
fourthStudying = Event("Studying", datetime(2019, 1, 28, 11, 00), 30)
fifthStudying = Event("Studying", datetime(2019, 1, 17, 17, 00), 90)
sixthStudying = Event("Studying", datetime(2019, 1, 15, 11, 00), 30)

calendar.append(firstStudying)
calendar.append(secondStudying)
calendar.append(thirdStudying)
calendar.append(fourthStudying)
calendar.append(fifthStudying)
calendar.append(sixthStudying)

# -- end of pre-populated data --
