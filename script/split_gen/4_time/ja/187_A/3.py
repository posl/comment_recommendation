def solve():
    a, b = map(int, input().split())
    print(max(sum([int(c) for c in str(a)]), sum([int(c) for c in str(b)])))
