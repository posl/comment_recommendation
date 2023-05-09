def main():
    A,B,K = map(int,input().split())
    x = A
    for i in range(K):
        if x >= B:
            break
        x = x * K
    print(i)
