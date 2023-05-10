def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    max_A = max(A)
    max_B = max(B)
    if max_A > max_B:
        print("Yes")
    else:
        print("No")
