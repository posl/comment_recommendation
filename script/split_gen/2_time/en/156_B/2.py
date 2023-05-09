def main():
    N, K = map(int, input().split())
    if N == 0:
        print(1)
    else:
        print(len(str(N).replace('0', '')))
