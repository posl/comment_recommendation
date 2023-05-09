def main():
    N = int(input())
    A = list(map(int, input().split()))
    min_height = 0
    for i in range(N):
        if A[i] > min_height + 1:
            print(-1)
            return
        elif A[i] == min_height + 1:
            min_height += 1
    print(N - min_height)
    return

if __name__ == '__main__':
    main()