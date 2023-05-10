def main():
    N = int(input())
    T = []
    A = []
    for i in range(N):
        t, k, *a = map(int, input().split())
        T.append(t)
        A.append(a)
    print(T)
    print(A)
