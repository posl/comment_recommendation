def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]
    A = [a%K for a in A]
    cnt = 0
    dic = {}
    for a in A:
        if a in dic:
            cnt += dic[a]
            dic[a] += 1
        else:
            dic[a] = 1
    print(cnt)

if __name__ == '__main__':
    main()