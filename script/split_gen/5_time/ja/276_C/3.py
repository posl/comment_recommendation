def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.sort()
    print(*p)
