def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count1 = 0
    count2 = 0
    for i in range(n):
        if A[i] == B[i]:
            count1 += 1
    for i in range(n):
        for j in range(n):
            if A[i] == B[j] and i != j:
                count2 += 1
    print(count1)
    print(count2//2)

if __name__ == '__main__':
    main()