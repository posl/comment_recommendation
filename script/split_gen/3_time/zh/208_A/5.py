def solve():
    a, b = map(int, input().split())
    print("Yes" if 6 * a >= b and b >= a else "No")
    return 0
