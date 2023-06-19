def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        flag = True
        for j in range(N):
            if i != j and A[j] % A[i] == 0:
                flag = False
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()