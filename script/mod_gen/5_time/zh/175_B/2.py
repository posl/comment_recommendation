def triangle():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] < l[i] + l[j]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    triangle()