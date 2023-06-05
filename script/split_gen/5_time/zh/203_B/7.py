def main():
    N, K = map(int, input().split())
    result = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            result += i*100 + j
    print(result)
