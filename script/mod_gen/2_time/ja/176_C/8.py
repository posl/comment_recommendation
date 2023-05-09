def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A[::-1]
    max_height = 0
    count = 0
    for i in range(N):
        if A[i] > max_height:
            max_height = A[i]
        elif A[i] < max_height:
            count += max_height - A[i]
        else:
            continue
    print(count)

if __name__ == '__main__':
    main()