def divisors(n):
    l = []
    for i in range(1, n+1):
        if n%i == 0:
            l.append(i)
    return l
a, b, k = map(int, input().split())
div = divisors(a) + divisors(b)
div = list(set(div))
div.sort(reverse=True)
print(div[k-1])

if __name__ == '__main__':
    divisors()