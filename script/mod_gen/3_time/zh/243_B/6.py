def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    count_a = 0
    count_b = 0
    for i in range(N):
        if A[i] == B[i]:
            count_a += 1
    print(count_a)
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i] == B[j]:
                    count_b += 1
    print(count_b//2)

if __name__ == '__main__':
    main()