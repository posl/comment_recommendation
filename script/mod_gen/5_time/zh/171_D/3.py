def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    sum_a = sum(a)
    cnt = {}
    for i in a:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1
    for b, c in bc:
        if b not in cnt:
            print(sum_a)
            continue
        sum_a += (c - b) * cnt[b]
        print(sum_a)
        if c not in cnt:
            cnt[c] = cnt[b]
        else:
            cnt[c] += cnt[b]
        cnt[b] = 0

if __name__ == '__main__':
    main()