def problems200_b():
    N, K = map(int, input().split())
    for _ in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + '200')
    return N
print(problems200_b())

if __name__ == '__main__':
    problems200_b()