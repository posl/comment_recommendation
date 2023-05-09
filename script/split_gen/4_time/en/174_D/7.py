def main():
    N = int(input())
    S = list(input())
    W = S.count('W')
    R = N - W
    print(min(W, R))
main()
