def main():
    N = int(input())
    if N < 0:
        N = -N
    print(N % 998244353)
