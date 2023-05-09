def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif B == 0:
        print(N)
    else:
        q, r = divmod(N, A + B)
        print(q * A + min(r, A))
