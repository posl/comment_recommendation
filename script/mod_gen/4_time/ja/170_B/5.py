def solve():
    X, Y = map(int, input().split())
    for i in range(X+1):
        if i*4 + (X-i)*2 == Y:
            return 'Yes'
    return 'No'
print(solve())
