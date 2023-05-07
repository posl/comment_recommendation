def main():
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))
    p_list.sort()
    p_list.reverse()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += p_list[i] / 2
        else:
            ans += p_list[i]
    print(int(ans))
