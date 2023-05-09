def main():
    N = int(input())
    S = ""
    while N != 0:
        if N % 2 == 0:
            N //= 2
            S += "B"
        else:
            N -= 1
            S += "A"
    print(S[::-1])
