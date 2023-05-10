def main():
    s = input()
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i in range(len(day)):
        if day[i] == s:
            print(6 - i)
            break

if __name__ == '__main__':
    main()