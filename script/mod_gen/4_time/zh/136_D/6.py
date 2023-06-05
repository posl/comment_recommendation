def main():
    s = input()
    n = len(s)
    ans = [0]*n
    i = 0
    while i < n:
        if s[i] == 'L':
            #找到第一个R
            j = i
            while j < n and s[j] == 'L':
                j += 1
            #j是第一个R的位置
            #找到第一个L
            k = j
            while k < n and s[k] == 'R':
                k += 1
            #k是第一个L的位置
            #偶数个
            if (k - j) % 2 == 0:
                ans[j-1] += (k-j)//2
                ans[j] += (k-j)//2
            #奇数个
            else:
                ans[j-1] += (k-j+1)//2
                ans[j] += (k-j-1)//2
            i = k
        else:
            #找到第一个L
            j = i
            while j < n and s[j] == 'R':
                j += 1
            #j是第一个L的位置
            #找到第一个R
            k = j
            while k < n and s[k] == 'L':
                k += 1
            #k是第一个R的位置
            #偶数个
            if (k - j) % 2 == 0:
                ans[j-1] += (k-j)//2
                ans[j] += (k-j)//2
            #奇数个
            else:
                ans[j-1] += (k-j-1)//2
                ans[j] += (k-j+1)//2
            i = k
    print(*ans)

if __name__ == '__main__':
    main()