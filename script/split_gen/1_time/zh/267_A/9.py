def main():
    weeks = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    week = input()
    week_index = weeks.index(week)
    print(6 - week_index)
