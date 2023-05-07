def main():
    N = int(input())
    S = []
    while N != 0:
        S.append(str(N % 2))
        N = -(N // 2)
    if len(S) == 0:
        print("0")
    else:
        print("".join(S))
main()
