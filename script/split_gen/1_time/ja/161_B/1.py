def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) < 4 * M * A[-1]:
        print("No")
    else:
        print("Yes")
