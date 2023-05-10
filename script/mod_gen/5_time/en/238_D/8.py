def solve():
    a, s = map(int, input().split())
    if a > s:
        print('No')
        return
    if s % 2 == 0:
        print('Yes')
        return
    if s % 2 == 1 and a % 2 == 1:
        print('Yes')
        return
    print('No')
T = int(input())
for _ in range(T):
    solve()

if __name__ == '__main__':
    solve()