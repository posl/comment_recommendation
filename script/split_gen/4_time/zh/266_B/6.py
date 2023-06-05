def main():
    n = int(input())
    if n < 0:
        n = -n
    print(998244353 - n % 998244353)
