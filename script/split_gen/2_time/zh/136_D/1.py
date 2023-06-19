def main():
    s = input()
    s = s.replace('RL','R L')
    s = s.split(' ')
    ans = []
    for i in range(len(s)):
        ans.append(0)
    for i in range(len(s)):
        if s[i] == 'R':
            ans[i+1] += 1
        else:
            ans[i-1] += 1
    print(' '.join(map(str,ans)))
