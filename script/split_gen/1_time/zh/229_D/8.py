def main():
    s = input()
    k = int(input())
    ans = 0
    l = len(s)
    for i in range(l):
        if s[i] == 'X':
            if i == 0:
                ans += 1
            elif s[i-1] == 'X':
                ans += 1
    for i in range(k):
        if ans == l:
            break
        if ans == 0:
            ans += 1
        elif ans == 1:
            if s[0] == '.' and s[1] == '.':
                s = s[:0] + 'X' + s[1:]
                ans += 1
            elif s[0] == '.' and s[1] == 'X':
                s = s[:1] + 'X' + s[2:]
                ans += 1
            elif s[0] == 'X' and s[1] == '.':
                s = s[:0] + 'X' + s[1:]
                ans += 1
            elif s[0] == 'X' and s[1] == 'X':
                s = s[:1] + 'X' + s[2:]
                ans += 1
        elif ans == l-1:
            if s[l-2] == '.' and s[l-1] == '.':
                s = s[:l-1] + 'X'
                ans += 1
            elif s[l-2] == '.' and s[l-1] == 'X':
                s = s[:l-2] + 'X'
                ans += 1
            elif s[l-2] == 'X' and s[l-1] == '.':
                s = s[:l-1] + 'X'
                ans += 1
            elif s[l-2] == 'X' and s[l-1] == 'X':
                s = s[:l-2] + 'X'
                ans += 1
        else:
            if s[ans] == '.':
                if s[ans-1] == '.' and s[ans+1] == '.':
                    s = s[:ans] + 'X' + s[ans+1:]
                    ans += 1
                elif s[ans-1] == '.' and s[ans+1]
