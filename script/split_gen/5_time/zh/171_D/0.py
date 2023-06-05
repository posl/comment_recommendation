def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    a_sum = sum(a)
    cnt = {}
    for i in a:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    for b, c in bc:
        if b in cnt:
            a_sum += (c - b) * cnt[b]
            if c in cnt:
                cnt[c] += cnt[b]
            else:
                cnt[c] = cnt[b]
            cnt[b] = 0
        print(a_sum)
