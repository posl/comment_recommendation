def main():
    N, A, B = map(int, input().split())
    for i in range(A):
        for j in range(N):
            print("." * B, end="")
            print("#" * B, end="")
        print()
    for i in range(A):
        for j in range(N):
            print("#" * B, end="")
            print("." * B, end="")
        print()
