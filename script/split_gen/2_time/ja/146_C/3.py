def main():
    A, B, X = map(int, input().split())
    N = 10**9
    while N > 0:
        if A*N + B*len(str(N)) <= X:
            print(N)
            return
        else:
            N = N//10
