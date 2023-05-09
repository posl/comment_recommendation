def main():
    K = int(input())
    ans = []
    while K > 0:
        if K % 2 == 0:
            ans.append(2)
        else:
            ans.append(0)
        K = (K - 1) // 2
    ans.reverse()
    print(''.join(map(str, ans)))

if __name__ == '__main__':
    main()