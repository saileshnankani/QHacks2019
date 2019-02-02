class Day:

    def __init__(self, day):
        self.day = day
        self.time_slots = {"12:00am": [], "12:30am": [], "1:00am": [], "1:30am": [], "2:00am": [], "2:30am": [],
                           "3:00am": [], "3:30am": [], "4:00am": [], "4:30am": [], "5:00am": [], "5:30am": [], "6:00am": []}



def output_dict():
    i = 1
    dict_output = {}
    string = ""
    while i < 13:
        string = string + str(i)  + ":00am"
        string2 = string + str(i) + ":00pm"
        string3 = string + str(i) + ":30am"
        string4 = string + str(i) + ":30am"
        dict_output[string] = []
        dict_output[string2] = []
        dict_output[string3] = []
        dict_output[string4] = []
        i += 1
    print(dict_output)
    return dict_output


output_dict()