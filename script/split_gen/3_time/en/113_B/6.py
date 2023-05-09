def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 10**9
    ans_index = 0
    for i in range(n):
        if abs(t-h[i]*0.006-a) < ans:
            ans = abs(t-h[i]*0.006-a)
            ans_index = i+1
    print(ans_index)
