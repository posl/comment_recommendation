def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(m):
                if t[k] == s[i] + '_' + s[j]:
                    ans.append(s[i])
                    ans.append(s[j])
                    ans.append(t[k].split('_')[1])
                    break
                elif t[k] == s[j] + '_' + s[i]:
                    ans.append(s[j])
                    ans.append(s[i])
                    ans.append(t[k].split('_')[1])
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print(-1)
        return
    for i in range(n):
        if i == 0:
            continue
        for j in range(n):
            if j == 0:
                continue
            if s[i] + '_' + s[j] == ans[-1]:
                ans.append(s[i])
                ans.append(s[j])
                break
            elif s[j] + '_' + s[i] == ans[-1]:
                ans.append(s[j])
                ans.append(s[i])
                break
        else:
            continue
        break
    else:
        print(-1)
        return
    for i in range(n):
        if i == 0:
            continue
        for j in range(n):
            if j == 0:
                continue
            if s[i] + '_' + s[j] == ans[-1]:
                ans.append(s[i])
                ans.append(s[j])
                break
            elif s[j] + '_' + s[i] == ans[-1]:
                ans.append(s[j])
                ans.append(s[i])
                break
        else:
            continue
        break
    else:
        print(-1)
        return
    print('_'.join(ans))
