def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.reverse()
    for s in S:
        print(s)
