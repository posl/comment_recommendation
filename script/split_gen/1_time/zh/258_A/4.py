def main():
    # input
    K = int(input())
    # solve
    hour = 21
    minute = 0
    for i in range(K):
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
        if hour == 24:
            hour = 0
    # output
    print("{:02d}:{:02d}".format(hour, minute))
