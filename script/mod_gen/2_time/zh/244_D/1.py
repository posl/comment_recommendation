def solve(n):
    a = 1
    b = 2*n+1
    while True:
        print(a)
        x = int(input())
        if x == 0:
            break
        if x < a:
            a = x
        elif x > b:
            b = x
        else:
            if a == x-1:
                a = x
            else:
                b = x

if __name__ == '__main__':
    solve()