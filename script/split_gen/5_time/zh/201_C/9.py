def main():
    s = input()
    ans = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if s[i] == 'o' and s[j] == 'o' and s[k] == 'o' and s[l] == 'o':
                        ans += 1
                    elif s[i] == 'o' and s[j] == 'o' and s[k] == 'o' and s[l] == '?':
                        ans += 1
                    elif s[i] == 'o' and s[j] == 'o' and s[k] == '?' and s[l] == 'o':
                        ans += 1
                    elif s[i] == 'o' and s[j] == 'o' and s[k] == '?' and s[l] == '?':
                        ans += 1
                    elif s[i] == 'o' and s[j] == '?' and s[k] == 'o' and s[l] == 'o':
                        ans += 1
                    elif s[i] == 'o' and s[j] == '?' and s[k] == 'o' and s[l] == '?':
                        ans += 1
                    elif s[i] == 'o' and s[j] == '?' and s[k] == '?' and s[l] == 'o':
                        ans += 1
                    elif s[i] == 'o' and s[j] == '?' and s[k] == '?' and s[l] == '?':
                        ans += 1
                    elif s[i] == '?' and s[j] == 'o' and s[k] == 'o' and s[l] == 'o':
                        ans += 1
                    elif s[i] == '?' and s[j] == 'o' and s[k] == 'o' and s[l] == '?':
                        ans += 1
                    elif s[i] == '?' and s[j] == 'o' and s[k] == '?' and s[l] == 'o':
                        ans += 1
                    elif s[i] == '?' and s[j] == 'o' and s[k] == '?' and s[l] == '?':
                        ans += 1
                    elif s[i] == '?' and s[j] == '?' and s[k] == 'o'
