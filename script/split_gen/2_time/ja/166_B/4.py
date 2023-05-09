def main():
    N, K = map(int, input().split())
    cnt = [0 for i in range(N)]
    for i in range(K):
        d = int(input())
        for j in map(int, input().split()):
            cnt[j-1] += 1
    print(cnt.count(0))
