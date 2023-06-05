def f(n):
    if n < 10:
        return n
    else:
        n = str(n)
        if n[0] == '1':
            return 9 * f(int(n[1:])) + int(n[1:])
        else:
            return (int(n[0])-1) * f(int(n[1:])) + int(n[1:])
n = int(input())
print(f(n))
