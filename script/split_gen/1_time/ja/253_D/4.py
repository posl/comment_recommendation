def main():
    N, A, B = map(int, input().split())
    print(N - (N//A + N//B - N//lcm(A,B)))
