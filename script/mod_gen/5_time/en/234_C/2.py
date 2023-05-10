def main():
    K = int(input())
    ans = ''
    while K > 0:
        K, r = divmod(K, 2)
        ans = '2' + ans if r else '0' + ans
    print(ans)

if __name__ == '__main__':
    main()