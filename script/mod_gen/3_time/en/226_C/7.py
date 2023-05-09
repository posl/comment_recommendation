def main():
    N = int(input())
    T = []
    A = []
    for i in range(N):
        temp = list(map(int, input().split()))
        T.append(temp[0])
        A.append(temp[2:])
    time = [0 for i in range(N)]
    for i in range(N):
        if A[i] == []:
            time[i] = T[i]
        else:
            for j in A[i]:
                time[i] = max(time[i], time[j-1] + T[i])
    print(max(time))

if __name__ == '__main__':
    main()