def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if min(A) < min(B):
        print("No")
    else:
        print("Yes")
