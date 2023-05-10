def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    timeList = [A,B,C,D,E]
    timeList.sort()
    timeList = timeList[1:]
    time = 0
    for t in timeList:
        if t % 10 != 0:
            time += t + 10 - (t % 10)
        else:
            time += t
    print(time)

if __name__ == '__main__':
    main()