def shift_by_n(s, n):
    # Write your code here
    res = ""
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            res += chr(ord(s[i]) + n - 26)
        else:
            res += chr(ord(s[i]) + n)
    return res

if __name__ == '__main__':
    shift_by_n()