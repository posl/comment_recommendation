def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(min(A))
    else:
        print(1)
