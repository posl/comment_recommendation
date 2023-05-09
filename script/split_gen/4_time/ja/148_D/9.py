def main():
    N = int(input())
    a_list = list(map(int, input().split()))
    ans = -1
    if a_list[0] == 1 and a_list[-1] == 1:
        ans = 0
        for i in range(1, N):
            if a_list[i] - a_list[i-1] > 1:
                ans = -1
                break
            elif a_list[i] - a_list[i-1] == 1:
                ans += 1
    print(ans)
