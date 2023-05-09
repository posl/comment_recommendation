def main():
    k = int(input())
    hour = 21
    minute = 0
    minute += k
    if minute >= 60:
        hour += minute // 60
        minute %= 60
    print(f'{hour:02}:{minute:02}')

if __name__ == '__main__':
    main()