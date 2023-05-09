def main():
    s = input()
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_count = 0
    for i in range(len(day)):
        if s == day[i]:
            day_count = i
    print(5 - day_count)

if __name__ == '__main__':
    main()