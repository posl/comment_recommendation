def main():
    s = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for i in range(5):
        if s == week[i]:
            print(5 - i)
            exit()

if __name__ == '__main__':
    main()