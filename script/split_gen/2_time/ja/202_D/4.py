def main():
    A, B, K = map(int, input().split())
    a = "a"
    b = "b"
    if A == 0:
        print(b * B)
    elif B == 0:
        print(a * A)
    else:
        if A >= B:
            if K <= (A + B) * (A + B - 1) // 2 - (B - 1):
                print(a + main())
            else:
                print(b + main())
        else:
            if K <= (A + B) * (A + B - 1) // 2 - (A - 1):
                print(b + main())
            else:
                print(a + main())
