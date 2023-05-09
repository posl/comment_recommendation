def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        i_str = str(i)
        for j in range(1, N + 1):
            j_str = str(j)
            if i_str[-1] == j_str[0] and i_str[0] == j_str[-1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()