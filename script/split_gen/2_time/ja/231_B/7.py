def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    print(max(S, key=S.count))
