def main():
    A, B = map(int, input().split())
    if B >= 10**18:
        print(A)
        exit()
    if A <= B:
        print(A)
        exit()
    if A % B == 0:
        print(A/B)
        exit()
    if A < B * 2:
        print((A/B + 1))
        exit()
    print((A/B + 1 + (A%B - B) / (B+1)))
