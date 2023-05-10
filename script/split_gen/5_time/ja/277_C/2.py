def main():
    N = int(input())
    AB = []
    for _ in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))
    AB.sort(key=lambda x: x[1])
    ans = 0
    for a, b in AB:
        if ans < a:
            ans = b
    print(ans)
    return
