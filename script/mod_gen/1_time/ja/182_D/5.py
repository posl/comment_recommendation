def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_position = 0
    position = 0
    for i in range(N):
        position += A[i]
        max_position = max(max_position, position)
    print(max_position)

if __name__ == '__main__':
    main()