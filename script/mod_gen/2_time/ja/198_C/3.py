def solve():
    R, X, Y = map(int, input().split())
    if X**2 + Y**2 == R**2:
        return 1
    if X**2 + Y**2 <= R**2*4:
        return 2
    return -(-int((X**2 + Y**2)**(1/2))//R)
print(solve())
