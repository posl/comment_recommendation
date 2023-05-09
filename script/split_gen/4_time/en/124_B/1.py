def main():
    N = int(input())
    H = list(map(int, input().split()))
    H_max = 0
    ans = 0
    for h in H:
        if h >= H_max:
            ans += 1
            H_max = h
    print(ans)
