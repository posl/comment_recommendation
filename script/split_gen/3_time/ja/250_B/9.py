def main():
    N, A, B = map(int, input().split())
    w = ["." for i in range(A * N)]
    b = ["#" for i in range(A * N)]
    for i in range(B * N):
        if i % 2 == 0:
            for j in range(A * N):
                print(w[j], end="")
            print()
        else:
            for j in range(A * N):
                print(b[j], end="")
            print()
