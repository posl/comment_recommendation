def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[-1] + L[i])
    print(sum(1 for i in D if i <= X))
