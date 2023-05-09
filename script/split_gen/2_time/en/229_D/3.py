def main():
    s = input()
    k = int(input())
    l = len(s)
    if l == 1:
        print(k//2)
        return
    if k == 0:
        print(s.count('X'))
        return
    if s[0] == 'X':
        i = 1
        while i < l and s[i] == 'X':
            i += 1
        if i == l:
            print(l*k//2)
            return
        ans = i//2
        i += 1
    else:
        ans = 0
        i = 0
    while i < l:
        j = i
        while j < l and s[j] == '.':
            j += 1
        ans += (j-i-1)//2
        i = j+1
    print(ans+k)
