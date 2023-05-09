def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 1:
            S = "A" + S
            N -= 1
        else:
            S = "B" + S
            N //= 2
    print(S)
main()
