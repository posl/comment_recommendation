def main():
    N = int(input())
    P = list(map(int,input().split()))
    cnt = 0
    for i in range(N):
        if P[i] == i:
            cnt += 1
            if i < N-1:
                P[i+1] = i+1
            else:
                P[0] = 0
    print(cnt)

if __name__ == '__main__':
    main()