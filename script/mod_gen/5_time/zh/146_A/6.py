def main():
    week = input()
    week_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - week_list.index(week))

if __name__ == '__main__':
    main()