def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0,0)
    print(N - P.index(max(P)))
