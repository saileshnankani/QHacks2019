class Day:

    def __init__(self, day):
        self.day = day
        self.time_slots = {'1:00am': [], '1:00pm': [], '1:30am': [], '2:00am': [], '2:00pm': [], '2:30am': [],
                           '3:00am': [], '3:00pm': [], '3:30am': [], '4:00am': [], '4:00pm': [], '4:30am': [],
                           '5:00am': [], '5:00pm': [], '5:30am': [], '6:00am': [], '6:00pm': [], '6:30am': [],
                           '7:00am': [], '7:00pm': [], '7:30am': [], '8:00am': [], '8:00pm': [], '8:30am': [],
                           '9:00am': [], '9:00pm': [], '9:30am': [], '10:00am': [], '10:00pm': [], '10:30am': [],
                           '11:00am': [], '11:00pm': [], '11:30am': [], '12:00am': [], '12:00pm': [], '12:30am': []}



def output_dict():
    i = 1
    dict_output = {}
    string = ""
    string2 = ""
    string3 = ""
    string4 = ""
    while i < 13:
        string = string + str(i)  + ":00am"
        string2 = string2 + str(i) + ":00pm"
        string3 = string3 + str(i) + ":30am"
        string4 = string4 + str(i) + ":30am"
        dict_output[string] = []
        dict_output[string2] = []
        dict_output[string3] = []
        dict_output[string4] = []
        string = ""
        string2 = ""
        string3 = ""
        string4 = ""
        i += 1
    print(dict_output)
    return dict_output


output_dict()