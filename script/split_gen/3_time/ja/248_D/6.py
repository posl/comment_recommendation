def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    lrx = [list(map(int, input().split())) for _ in range(q)]
    
    cnt = [0] * (n + 1)
    for i in a:
        cnt[i] += 1
    for i in range(q):
        l, r, x = lrx[i]
        print(cnt[x])
