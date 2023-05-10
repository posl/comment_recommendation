def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s.append("")
    max = 0
    count = 0
    for i in range(n):
        if s[i] == s[i+1]:
            count += 1
        else:
            if count > max:
                max = count
                ans = s[i]
            count = 0
    print(ans)
