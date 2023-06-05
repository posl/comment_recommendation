def solve():
    N = int(input())
    result = N // 2
    if N % 2 == 1:
        result += 1
    print(result)

if __name__ == '__main__':
    solve()