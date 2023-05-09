def main():
    N = int(input())
    cnt = 0
    for p in range(2, N):
        if N % p == 0:
            cnt += 1
            N /= p
            while N % p == 0:
                N /= p
        if N == 1:
            break
    if N != 1:
        cnt += 1
    print(cnt)
