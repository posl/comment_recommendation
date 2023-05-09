def main():
    N = int(input())
    if N % 998244353 == 0:
        print(0)
    else:
        print(998244353 - (N % 998244353))
