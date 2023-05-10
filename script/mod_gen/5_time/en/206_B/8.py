def myCode():
    n = int(input())
    sum = 0
    day = 0
    while(sum < n):
        day += 1
        sum += day
    print(day)
    return

if __name__ == '__main__':
    myCode()