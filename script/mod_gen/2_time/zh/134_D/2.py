def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max_value = max(A)
    max_index = A.index(max_value)
    for i in range(N):
        if i == max_index:
            print(max(A[:max_index] + A[max_index + 1:]))
        else:
            print(max_value)

if __name__ == '__main__':
    main()