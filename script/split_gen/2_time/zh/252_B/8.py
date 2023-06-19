def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    Amax = max(A)
    if Amax in B:
        print("No")
    else:
        print("Yes")
