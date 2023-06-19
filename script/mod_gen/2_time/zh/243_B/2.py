def main():
    N = int(input())
    A = input().split()
    B = input().split()
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        if A[i] == B[i]:
            cnt1 += 1
    for i in range(N):
        for j in range(N):
            if A[i] == B[j] and i != j:
                cnt2 += 1
    print(cnt1)
    print(cnt2)

if __name__ == '__main__':
    main()