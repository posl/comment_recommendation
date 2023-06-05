def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    
    sum_a = sum(a)
    cnt = [0] * 100001
    for i in a:
        cnt[i] += 1
    
    for b, c in bc:
        sum_a -= cnt[b] * b
        sum_a += cnt[b] * c
        cnt[c] += cnt[b]
        cnt[b] = 0
        print(sum_a)

if __name__ == '__main__':
    main()