def S(n):
    if n == 1:
        return [1]
    else:
        s = S(n-1)
        return s + [n] + s
N = int(input())
print(*S(N))

if __name__ == '__main__':
    S()