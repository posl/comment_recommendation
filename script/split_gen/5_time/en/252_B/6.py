def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_a = max(A)
    max_b = max(B)
    if max_a > max_b:
        print("Yes")
    else:
        print("No")
