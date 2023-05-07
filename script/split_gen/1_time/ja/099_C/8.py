def main():
    N = int(input())
    print(min(coin(N, 1), coin(N, 6), coin(N, 9)))
