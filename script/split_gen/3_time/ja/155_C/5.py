def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    max = 0
    ans = []
    for i in range(n):
        if s.count(s[i]) > max:
            max = s.count(s[i])
    for i in range(n):
        if s.count(s[i]) == max:
            ans.append(s[i])
    ans = list(set(ans))
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])
