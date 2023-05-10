def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i, a in enumerate(A):
        B[a - 1] = i + 1
    print(*B)

if __name__ == '__main__':
    main()