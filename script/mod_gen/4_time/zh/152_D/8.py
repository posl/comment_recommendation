def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 10 == 0:
            continue
        else:
            str_i = str(i)
            if str_i[0] == str_i[-1]:
                ans += 1
            for j in range(i+1, N+1):
                str_j = str(j)
                if str_i[-1] == str_j[0] and str_j[-1] == str_i[0]:
                    ans += 2
    print(ans)

if __name__ == '__main__':
    main()