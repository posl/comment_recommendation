def main():
    s,k = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    ans = []
    for i in range(len(s)):
        tmp = s[i]
        s.pop(i)
        ans.append(tmp)
        ans.extend(sorted(s))
        s.insert(i,tmp)
    ans = sorted(set(ans))
    print("".join(ans[k-1]))
