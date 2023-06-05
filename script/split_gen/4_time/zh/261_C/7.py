def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s2 = []
    for i in range(n):
        if s[i] in s2:
            cnt = 1
            for j in range(len(s2)):
                if s[i] == s2[j]:
                    cnt += 1
            s2.append(s[i] + "(" + str(cnt) + ")")
        else:
            s2.append(s[i])
    for i in range(len(s2)):
        print(s2[i])
