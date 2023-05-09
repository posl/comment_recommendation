def solve():
    A, B = map(int, input().split())
    if B == 1:
        print(A)
        return
    if A == 1:
        print(1)
        return
    if A == 2:
        print(2)
        return
    # (A/((g)^(1/2))) = B*t + A
    # (g)^(1/2) = A/(B*t+A)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    t = 1
    while True:
        g = A**2/(B**2*t**2 + 2*A*B*t + A**2)
        if g < 1:
            print(t + A/(g**0.5))
            return
        t += 1

if __name__ == '__main__':
    solve()