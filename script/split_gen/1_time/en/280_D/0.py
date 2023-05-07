def main():
    K = int(input())
    N = K
    i = 2
    while i * i <= K:
        if K % i == 0:
            while K % i == 0:
                K = K // i
            N = N // i * (i - 1)
        i += 1
    if K > 1:
        N = N // K * (K - 1)
    print(N)
