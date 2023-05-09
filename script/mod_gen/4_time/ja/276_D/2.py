def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        if all([a % 2 == 0 for a in A]):
            ans += 1
            A = [a // 2 for a in A]
        elif any([a % 2 == 0 for a in A]):
            print(ans)
            exit()
        else:
            break
    print(ans)

if __name__ == '__main__':
    solve()