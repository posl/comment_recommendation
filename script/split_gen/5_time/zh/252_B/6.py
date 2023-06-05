def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(set(A) - set(B)) > 0:
        print("Yes")
    else:
        print("No")
