def main():
    n = int(input())
    n_str = str(n)
    n_len = len(n_str)
    #print(n, n_str, n_len)
    ans = 0
    for i in range(1, n_len+1):
        #print(i)
        if i == n_len:
            ans += n - (10**(i-1)) + 1
        else:
            ans += 9 * (10**(i-1)) * i
    print(ans%998244353)

if __name__ == '__main__':
    main()