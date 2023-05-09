def main():
    N,K = map(int,input().split())
    result = 0
    while N > 0:
        N = N // K
        result += 1
    print(result)
