def main():
    N, K = map(int, input().split())
    a = N
    for i in range(K):
        a = f(a)
    print(a)
