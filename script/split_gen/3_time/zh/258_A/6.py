def main():
    K = int(input())
    hour = 21
    minute = 0
    for i in range(K):
        minute += 1
        if minute == 60:
            hour += 1
            minute = 0
        if hour == 24:
            hour = 0
    if hour < 10 and minute < 10:
        print('0' + str(hour) + ':' + '0' + str(minute))
    elif hour < 10:
        print('0' + str(hour) + ':' + str(minute))
    elif minute < 10:
        print(str(hour) + ':' + '0' + str(minute))
    else:
        print(str(hour) + ':' + str(minute))
