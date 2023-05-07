def pascal(n):
    if n == 0:
        return [1]
    else:
        p = pascal(n-1)
        return [1] + [p[i] + p[i+1] for i in range(n-1)] + [1]
N = int(input())
for i in range(N):
    print(*pascal(i))

if __name__ == '__main__':
    pascal()