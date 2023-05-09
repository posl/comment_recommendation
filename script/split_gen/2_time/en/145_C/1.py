def main():
    import itertools
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in itertools.permutations(range(n)):
        for j in range(n-1):
            ans += ((x[i[j]] - x[i[j+1]])**2 + (y[i[j]] - y[i[j+1]])**2)**0.5
    print(ans / math.factorial(n))
