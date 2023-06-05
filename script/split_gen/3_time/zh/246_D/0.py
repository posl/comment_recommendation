def main():
    n = int(input())
    #print(n)
    a = 0
    b = 0
    x = 0
    while x < n:
        a = a + 1
        b = 0
        while x < n:
            b = b + 1
            x = a**3 + a**2*b + a*b**2 + b**3
            if x >= n:
                break
        if x >= n:
            break
    print(x)
