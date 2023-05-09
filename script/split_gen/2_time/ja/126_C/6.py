def main():
    N, K = map(int, input().split())
    if N < K:
        print((1/N) * ((1/2)**(int(math.log(K, 2)))))
    else:
        print(1 - ((N-K+1)/N))
