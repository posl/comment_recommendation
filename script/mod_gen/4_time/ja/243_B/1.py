def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count1 += 1
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] == B[j]:
                count2 += 1
    print(count1)
    print(count2//2)

if __name__ == '__main__':
    main()