def main():
    day = input()
    week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    for i in range(7):
        if day == week[i]:
            print(7 - i)
            break
