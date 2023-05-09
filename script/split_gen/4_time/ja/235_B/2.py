def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if h_list[i] < h_list[i+1]:
            ans = 0
        else:
            ans += 1
    print(ans)
