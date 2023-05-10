def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]
    for i in a:
        b.append(b[-1] + i)
    ans = float('inf')
    for i in range(1, n - 2):
        j = bisect.bisect_left(b, b[i] / 2)
        k = bisect.bisect_left(b, (b[i] + b[-1]) / 2)
        ans = min(ans, abs(b[i] - 2 * b[j]), abs(b[i] - 2 * (b[k] - b[i])))
    print(ans)
