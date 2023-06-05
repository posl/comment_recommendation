def solve(a, b, k):
    if a == 0:
        return "b" * b
    elif b == 0:
        return "a" * a
    else:
        count = [[0] * (b + 1) for _ in range(a + 1)]
        count[0][0] = 1
        for i in range(a + 1):
            for j in range(b + 1):
                if i > 0:
                    count[i][j] += count[i - 1][j]
                if j > 0:
                    count[i][j] += count[i][j - 1]
        result = ""
        while a > 0 and b > 0:
            if k <= count[a - 1][b]:
                result += "a"
                a -= 1
            else:
                result += "b"
                k -= count[a - 1][b]
                b -= 1
        if a > 0:
            result += "a" * a
        else:
            result += "b" * b
        return result

if __name__ == '__main__':
    solve()