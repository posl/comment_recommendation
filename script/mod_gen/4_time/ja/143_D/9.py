def triangle_count(n, l):
    l.sort()
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    cnt += 1
    return cnt
n = int(input())
l = list(map(int, input().split()))
print(triangle_count(n, l))

if __name__ == '__main__':
    triangle_count()