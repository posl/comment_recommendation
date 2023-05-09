def main():
    k = int(input())
    hour = 21
    minute = 0
    if k <= 60:
        minute += k
    elif k > 60:
        hour += 1
        minute = k - 60
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 24:
        hour = 0
    print(f'{hour:02d}:{minute:02d}')
main()
