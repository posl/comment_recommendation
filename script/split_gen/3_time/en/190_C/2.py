def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]
    def f(s):
        a = [0] * (n + 1)
        for i in range(k):
            if (s >> i) & 1:
                a[cd[i][0]] += 1
            else:
                a[cd[i][1]] += 1
        return sum(a[ab[i][0]] > 0 and a[ab[i][1]] > 0 for i in range(m))
    print(max(f(s) for s in range(1 << k)))
main()
Hi, I'm a beginner in python and I'm trying to solve this problem. I'm not sure if I'm doing it right. This is my code:
