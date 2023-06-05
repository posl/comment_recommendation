def solution(N):
    a = 0
    b = 0
    c = 0
    d = 0
    while True:
        if a**3+a**2*b+a*b**2+b**3 >= N:
            break
        else:
            a += 1
            b += 1
    while True:
        if a**3+a**2*b+a*b**2+b**3 == N:
            c = a
            d = b
            break
        elif a**3+a**2*b+a*b**2+b**3 > N:
            a -= 1
        elif a**3+a**2*b+a*b**2+b**3 < N:
            b -= 1
    return c**3+c**2*d+c*d**2+d**3

if __name__ == '__main__':
    solution()