def main():
    s = input()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in range(7):
        if s == days[i]:
            print(7 - i)
            break

if __name__ == '__main__':
    main()