def main():
    N, K = map(int, input().split())
    d = [0] * N
    for i in range(K):
        di = int(input())
        for j in map(int, input().split()):
            d[j-1] += 1
    print(d.count(0))
