def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if A[i]*A[j] == A[k]:
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()