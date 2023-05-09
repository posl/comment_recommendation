def main():
    n = int(input())
    s = input()
    
    ans = [0]
    for i in range(1, n):
        if s[i-1] == 'R' and s[i] == 'L':
            ans.append(i+1)
        elif s[i-1] == 'L' and s[i] == 'R':
            ans.append(i)
        else:
            ans.append(0)
    ans.append(0)
    
    print(' '.join(map(str, ans)))
