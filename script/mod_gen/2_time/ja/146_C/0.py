def main():
    A, B, X = map(int, input().split())
    N = 0
    if X >= A * 10**9 + B * 10:
        N = 10**9
    else:
        for i in range(9):
            if X >= A * 10**(8-i) + B * (9-i):
                N = 10**(8-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(7-i)) + B * (9-i):
                N += 10**(7-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(6-i)) + B * (9-i):
                N += 10**(6-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(5-i)) + B * (9-i):
                N += 10**(5-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(4-i)) + B * (9-i):
                N += 10**(4-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(3-i)) + B * (9-i):
                N += 10**(3-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(2-i)) + B * (9-i):
                N += 10**(2-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(1-i)) + B * (9-i):
                N += 10**(1-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(0-i)) + B * (9-i):
                N += 10**(0-i)
                break
    print(N)

if __name__ == '__main__':
    main()