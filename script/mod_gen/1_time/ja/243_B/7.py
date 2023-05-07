def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = dict()
    B_dict = dict()
    for i in range(N):
        A_dict[A[i]] = i
        B_dict[B[i]] = i
    count = 0
    for i in range(N):
        if A[i] == B[i]:
            count += 1
    print(count)
    count = 0
    for i in range(N):
        if A_dict[A[i]] != B_dict[A[i]]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()