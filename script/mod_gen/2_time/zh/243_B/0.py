def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    # print(A)
    # print(B)
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count1 += 1
    for i in range(N):
        for j in range(N):
            if i != j and A[i] == B[j]:
                count2 += 1
    print(count1)
    print(count2)

if __name__ == '__main__':
    main()