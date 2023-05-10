def main():
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if n < b:
        print(0)
    elif a == b:
        print(1)
    else:
        # nCkを求める
        # nCk = n! / k! / (n-k)!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) * (n-k)! / k! / (n-k)!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k * (k-1) * (k-2) * ... * 1
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k * (k-1) * (k-2) * ... * 1
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k * (k-1) * (k-2) * ... * 1
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k * (k-1) * (k-2) * ... * 1
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k
