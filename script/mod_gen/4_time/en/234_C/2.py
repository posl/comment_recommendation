def main():
    K = int(input())
    if K == 1:
        print(2)
        return
    else:
        K -= 1
        ans = ''
        while K > 0:
            ans = str(K % 2) + ans
            K //= 2
        ans = ans.replace('0', '2')
        print(ans)

if __name__ == '__main__':
    main()