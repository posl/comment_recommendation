def main():
    n = int(input())
    a = list(map(int, input().split()))
    # a = [int(i) for i in input().split()]
    # a = input().split()
    # a = list(map(int, input().split()))
    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]
    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]
    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]
    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]
    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]
    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]
    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]
    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]
    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]
    ans = 0
    c = 0
    m = 1000000000
    for i in range(n):
        ans += abs(a[i])
        if a[i] < 0:
            c += 1

if __name__ == '__main__':
    main()