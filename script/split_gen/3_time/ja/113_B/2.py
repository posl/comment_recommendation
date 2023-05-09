def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    d = []
    for i in range(N):
        d.append(abs(A - (T - H[i] * 0.006)))
    print(d.index(min(d)) + 1)
