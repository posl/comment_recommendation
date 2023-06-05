def main():
    n = int(input())
    a = list(map(int, input().split()))
    from collections import Counter
    c = Counter(a)
    ans = [0] * n
    for k, v in c.items():
        ans[k-1] = v * (v-1) // 2
    for i in a:
        print(sum(ans) - ans[i-1])

if __name__ == '__main__':
    main()