def main():
    N = int(input())
    print(N - 1 - int(N ** 0.5) - int(N ** 0.25) + int(N ** 0.5 * 0.5))
