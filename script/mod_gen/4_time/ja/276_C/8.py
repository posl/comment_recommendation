def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        count += p[i] * 10 ** i
    count -= 1
    q = list(map(int, str(count)))
    q.sort()
    q.reverse()
    for i in range(n):
        print(q[i], end=' ')
    print()
main()
