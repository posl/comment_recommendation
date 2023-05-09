def main():
    A, B = map(int, input().split())
    if A <= B:
        print(A)
        return
    g = 1
    ans = float('inf')
    for i in range(100):
        ans = min(ans, i + A / (g ** 0.5))
        g += 1
    print(ans)
