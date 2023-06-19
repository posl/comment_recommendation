def solve(n, x, y):
    result = [0] * n
    for i in range(1, n):
        for j in range(i+1, n+1):
            d = min(j-i, abs(x-i)+1+abs(y-j), abs(y-i)+1+abs(x-j))
            result[d] += 1
    return result[1:]
