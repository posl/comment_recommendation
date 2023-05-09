def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for s in S[::-1]:
        print(s)
