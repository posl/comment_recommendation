def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    a = 0
    b = 0
    while True:
        if a**3 + a**2*b + a*b**2 + b**3 >= N:
            break
        if a**3 + a**2*b + a*b**2 + b**3 < N:
            a += 1
            b = 0
        while a**3 + a**2*b + a*b**2 + b**3 < N:
            b += 1
    print(a**3 + a**2*b + a*b**2 + b**3)
