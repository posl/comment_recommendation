def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(-1)
    cnt = 0
    tmp = 0
    for i in range(N-1):
        if A[i] == A[i+1]:
            tmp += 1
        else:
            cnt += tmp*(tmp+1)//2
            tmp = 0
    print(cnt)

if __name__ == '__main__':
    main()