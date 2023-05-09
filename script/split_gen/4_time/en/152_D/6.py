def main():
    N = input()
    N = int(N)
    ans = 0
    for i in range(1, N + 1):
        i_str = str(i)
        i_len = len(i_str)
        if i_len == 1:
            ans += 1
        else:
            if i_str[0] == i_str[-1]:
                ans += 1
    print(ans)
