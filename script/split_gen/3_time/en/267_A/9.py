def main():
    #Read in the day of the week
    day = input()
    #Create a dictionary to map the day of the week to an integer
    days = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4}
    print(5 - days[day])
