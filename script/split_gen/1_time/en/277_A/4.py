def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N):
        if X == P[i]:
            print(i+1)
            break
