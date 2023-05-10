def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    #print(T)
    time1 = 0
    time2 = 0
    for i in range(N):
        if time1 > time2:
            time2 += T[i]
        else:
            time1 += T[i]
    print(max(time1, time2))

if __name__ == '__main__':
    main()