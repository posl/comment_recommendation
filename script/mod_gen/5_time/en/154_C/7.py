def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == len(a):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()