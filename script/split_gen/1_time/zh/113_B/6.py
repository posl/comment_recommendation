def main():
    N = int(input())
    T,A = map(int,input().split())
    H = list(map(int,input().split()))
    h = []
    for i in range(N):
        h.append(abs(A - (T - H[i]*0.006)))
    print(h.index(min(h)) + 1)
