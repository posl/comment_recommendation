def main():
    A, B = map(int, input().split())
    g = 1
    t = 0
    while A/((g+1)**0.5) > A/(g**0.5) + B:
        g += 1
        t += B
    t += A/((g)**0.5)
    print(t)
