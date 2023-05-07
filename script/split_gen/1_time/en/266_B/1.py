def main():
    N = int(input())
    print((N - N // 998244353 * 998244353) % 998244353)
