def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A+B == 0:
        print(0)
    else:
        print(min(N//A, N//(A+B)*A + N%(A+B)))
