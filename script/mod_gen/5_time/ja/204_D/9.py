def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    T1 = []
    T2 = []
    for i in range(N):
        if sum(T1) <= sum(T2):
            T1.append(T[i])
        else:
            T2.append(T[i])
    print(max(sum(T1), sum(T2)))

if __name__ == '__main__':
    main()