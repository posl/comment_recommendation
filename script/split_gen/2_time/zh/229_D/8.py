def main():
    s = input()
    k = int(input())
    s0 = s.replace('.', ' ')
    s1 = s0.split()
    s2 = list(map(len, s1))
    l = len(s2)
    if l == 1:
        if s[0] == '.':
            if k == 0:
                print(0)
            else:
                print(min(k, s2[0]))
        else:
            print(s2[0])
    else:
        if s[0] == '.':
            if k == 0:
                print(s2[0])
            else:
                print(min(k, s2[0]))
        else:
            ans = s2[0]
            for i in range(1, l):
                ans = max(ans, s2[i - 1] + s2[i])
            if s[-1] == '.':
                ans = max(ans, s2[-1])
            else:
                ans = max(ans, s2[-1] + min(k, s2[-1]))
            print(ans)
