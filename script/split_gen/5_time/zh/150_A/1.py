def main():
    K, X = input().split()
    K = int(K)
    X = int(X)
    if X >= K*500:
        print("Yes")
    else:
