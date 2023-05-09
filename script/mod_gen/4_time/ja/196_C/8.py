def main():
    N = int(input())
    N_len = len(str(N))
    ans = 0
    for i in range(1, N+1):
        i_str = str(i)
        i_str_len = len(i_str)
        if i_str_len % 2 == 0:
            i_str_first = i_str[:i_str_len//2]
            i_str_second = i_str[i_str_len//2:]
            if i_str_first == i_str_second:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()