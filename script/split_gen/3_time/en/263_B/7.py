def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    print(solve(n, p))
