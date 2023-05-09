def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    avg_temp = [T - h * 0.006 for h in H]
    min_diff = float('inf')
    ans = 0
    for i, temp in enumerate(avg_temp, 1):
        diff = abs(temp - A)
        if diff < min_diff:
            min_diff = diff
            ans = i
    print(ans)
