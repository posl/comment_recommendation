def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = dict(zip(A, range(N)))
    B_dict = dict(zip(B, range(N)))
    count = 0
    for i in range(N):
        if A_dict[A[i]] == B_dict[A[i]]:
            count += 1
    print(count)
    print(N - count - len(set(A) & set(B)))

if __name__ == '__main__':
    main()