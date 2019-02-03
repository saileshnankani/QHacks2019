from _datetime import datetime
from datetime import timedelta
from Events import Event
import collections


calendar = []

today = datetime.now()

# -- pre-populated habit-tracker

monday = Day('Monday')
tuesday = Day('Tuesday')
wednesday = Day('Wednesday')
thursday = Day('Thursday')
friday = Day('Friday')
saturday = Day('Saturday')
sunday = Day('Sunday')

monday.time_slots = {1.0: ["Meeting", "Studying", "Homework", "Meeting","Homework", "Homework"], 13.5: ["Studying", "Studying", "Stuyding", "Projects", "Errands"]}
tuesday.time_slots = {12.0: ["Meeting", "Errands", "Errands", "Errands", "Errands", "Meeting"], 13.5: ["TestPrep", "TestPrep", "TestPrep", "Projects", "Errands"]}
wednesday.time_slots = {1.0: ["Meeting", "Meeting", "Meeting", "Meeting","Homework", "Homework"], 13.5: ["Studying", "Studying", "Stuyding", "Projects", "Errands"]}
thursday.time_slots = {1.0: ["Meeting", "Studying", "Homework", "Meeting","Homework", "Homework"], 13.5: ["Studying", "Studying", "Stuyding", "Projects", "Errands"]}
friday.time_slots = {12.0: ["Meeting", "Studying", "Homework", "Meeting","Homework", "Homework"], 12.5: ["Studying", "Studying", "Stuyding", "Projects", "Errands"]}
saturday.time_slots = {5.0: ["Studying", "Studying", "Studying", "Meeting","Homework", "Homework"], 13.5: ["Laundry", "Laundry", "Laundry", "Projects", "Errands"]}
sunday.time_slots = {12.0: ["Meeting", "Studying", "Laundry", "Meeting","Homework", "Homework"], 12.5: ["Errands", "Studying", "Errands", "Projects", "Errands"]}



# -- end of pre-populated habit tracker

# -- pre-populated data --

firstHomework = Event("Homework", datetime(2019, 1, 4, 15, 30), 30, datetime(2019, 1, 4, 15, 30))
secondHomework = Event("Homework", datetime(2019, 1, 6, 12, 00), 60, datetime(2019, 1, 6, 12, 00))
thirdHomework = Event("Homework", datetime(2019, 1, 8, 15, 30), 30, datetime(2019, 1, 8, 15, 30))
fourthHomework = Event("Homework", datetime(2019, 1, 11, 15, 20), 30, datetime(2019, 1, 11, 15, 20))
fifthHomework = Event("Homework", datetime(2019, 1, 13, 12, 00), 60, datetime(2019, 1, 13, 12, 00))
sixthHomework = Event("Homework", datetime(2019, 1, 15, 15, 30), 30, datetime(2019, 1, 15, 15, 30))

calendar.append(firstHomework)
calendar.append(secondHomework)
calendar.append(thirdHomework)
calendar.append(fourthHomework)
calendar.append(fifthHomework)
calendar.append(sixthHomework)

firstTestPrep = Event("TestPrep", datetime(2019, 1, 5, 19, 00), 30, datetime(2019, 1, 5, 19, 00))
secondTestPrep = Event("TestPrep", datetime(2019, 1, 7, 14, 30), 60, datetime(2019, 1, 7, 14, 30))
thirdTestPrep = Event("TestPrep", datetime(2019, 1, 4, 19, 00), 30, datetime(2019, 1, 4, 19, 00))
fourthTestPrep = Event("TestPrep", datetime(2019, 1, 6, 14, 30), 60, datetime(2019, 1, 6, 14, 30))
fifthTestPrep = Event("TestPrep", datetime(2019, 1, 8, 15, 30), 30, datetime(2019, 1, 8, 15, 30))

calendar.append(firstTestPrep)
calendar.append(secondTestPrep)
calendar.append(thirdTestPrep)
calendar.append(fourthTestPrep)
calendar.append(fifthTestPrep)

firstErrand = Event("Errands", datetime(2019, 1, 9, 17, 00), 30, datetime(2019, 1, 9, 17, 00))
secondErrand = Event("Errands", datetime(2019, 1, 10, 17, 00), 30, datetime(2019, 1, 10, 17, 00))
thirdErrand = Event("Errands", datetime(2019, 1, 11, 17, 00), 30,datetime(2019, 1, 11, 17, 00))
fourthErrand = Event("Errands", datetime(2019, 1, 12, 17, 00), 30, datetime(2019, 1, 12, 17, 00))

calendar.append(firstErrand)
calendar.append(secondErrand)
calendar.append(thirdErrand)
calendar.append(fourthErrand)

firstProject = Event("Projects", datetime(2019, 1, 6, 17, 00), 90, datetime(2019, 1, 6, 17, 00))
secondProject = Event("Projects", datetime(2019, 1, 7, 11, 00), 180, datetime(2019, 1, 7, 11, 00))
thirdProject = Event("Projects", datetime(2019, 1, 8, 17, 00), 90, datetime(2019, 1, 8, 17, 00))
fourthProject = Event("Projects", datetime(2019, 1, 9, 11, 00), 180, datetime(2019, 1, 9, 11, 00))
fifthProject = Event("Projects", datetime(2019, 1, 10, 17, 00), 90, datetime(2019, 1, 10, 17, 00))
sixthProject = Event("Projects", datetime(2019, 1, 11, 11, 00), 180, datetime(2019, 1, 11, 11, 00))

calendar.append(firstHomework)
calendar.append(secondHomework)
calendar.append(thirdHomework)
calendar.append(fourthHomework)
calendar.append(fifthHomework)
calendar.append(sixthHomework)

secondStudying = Event("Studying", datetime(2019, 1, 7, 11, 00), 30, datetime(2019, 1, 7, 11, 00))
firstStudying = Event("Studying", datetime(2019, 1, 6, 17, 00), 90, datetime(2019, 1, 6, 17, 00))
thirdStudying = Event("Studying", datetime(2019, 1, 8, 17, 00), 90, datetime(2019, 1, 8, 17, 00))
fourthStudying = Event("Studying", datetime(2019, 1, 9, 11, 00), 30, datetime(2019, 1, 9, 11, 00))
fifthStudying = Event("Studying", datetime(2019, 1, 10, 17, 00), 90, datetime(2019, 1, 10, 17, 00))
sixthStudying = Event("Studying", datetime(2019, 1, 11, 11, 00), 30, datetime(2019, 1, 11, 11, 00))

calendar.append(firstStudying)
calendar.append(secondStudying)
calendar.append(thirdStudying)
calendar.append(fourthStudying)
calendar.append(fifthStudying)
calendar.append(sixthStudying)

# -- end of pre-populated data --


# -- begin processing of data --


sorted(calendar)

for i in calendar:
    print(i.date_scheduled)




# -- end processing of data --




class Day:

    def __init__(self, day):
        self.day = day
        self.time_slots = {1.0: [], 13.0: [], 1.5: [], 13.5: [], 2.0: [], 14.0: [], 2.5: [], 14.5: [],
                            3.0: [], 15.0: [], 3.5: [], 15.5: [], 4.0: [], 16.0: [], 4.5: [], 16.5: [],
                            5.0: [], 17.0: [], 5.5: [], 17.5: [], 6.0: [], 18.0: [], 6.5: [], 18.5: [],
                            7.0: [], 19.0: [], 7.5: [], 19.5: [], 8.0: [], 20.0: [], 8.5: [], 20.5: [],
                            9.0: [], 21.0: [], 9.5: [], 21.5: [], 10.0: [], 22.0: [], 10.5: [], 22.5: [],
                            11.0: [], 23.0: [], 11.5: [], 23.5: [], 12.0: [], 0.0: [], 12.5: [], 0.5: []}




def main(type, deadline):


    # ESTIMATE AMOUNT OF TIME

    # TODO: result_duration = need from database  (1 is equivalent to 30 min)                       1

    result_duration = 1

    # FIND SPACE ON CALENDAR

    # find frequency
    weekday = today.weekday()
    weekday_to_time_slot = {0: sunday, 1: monday, 2: tuesday, 3: wednesday, 4: thursday, 5: friday, 6: saturday, 7: sunday}
    current_day = today
    best_ones = []

    for i in range(7):
        # for each of the 48 spots / duration number of times in i, get a counter for the event we are looking for
        # and check which ones are available. Save the best duration (so time + duration) in a list
        for p in 48/result_duration:
            loop_count = result_duration/30

            total_in_duration = 0

            for n in loop_count:
                counts = collections.Counter(weekday_to_time_slot[weekday][n+p])
                sortedEvents = []
                for k in sorted(counts, key=counts.__getitem__, reverse=True):
                    sortedEvents.extend([k for _ in range(counts[k])])

                sortedEvents_new = []
                for item in sortedEvents:
                    if item not in sortedEvents_new:
                        sortedEvents_new.append(item)

                total_in_duration = total_in_duration + counts[0]   # add frequency of the most popular item


        best_ones.append(frequency, current_day)
        current_day = today+timedelta(days=1)
        weekday = weekday + 1
        weekday = weekday % 7

    max = 0
    max_datetime_frequency = ()

    for datetime_frequency_value in best_ones:
        if datetime_frequency_value[1] > max:
            max_datetime_frequency = datetime_frequency_value
            max = datetime_frequency_value[1]

     # TODO: update database here
     # TODO: update the calendar                                          2 : maintain sort

    return max_datetime_frequency[0], result_duration
