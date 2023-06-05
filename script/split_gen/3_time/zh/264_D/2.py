def minSwaps(s):
    s = list(s)
    ans = 0
    for i in range(len(s)):
        if s[i] == 'a':
            continue
        else:
            j = i + 1
            while j < len(s):
                if s[j] == 'a':
                    break
                else:
                    j += 1
            ans += j - i
            s[i:j+1] = ['a'] + s[i:j]
    return ans
