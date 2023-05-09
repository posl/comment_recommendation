def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    max_exp = 0
    for i in range(N-K+1):
        exp = sum(p[i:i+K])/(K/2)
        if exp > max_exp:
            max_exp = exp
    print(max_exp)
