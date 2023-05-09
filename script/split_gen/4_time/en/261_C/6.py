def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s2 = []
    for i in range(n):
        if s[i] not in s2:
            s2.append(s[i])
            print(s[i])
        else:
            count = 0
            for j in range(len(s2)):
                if s2[j] == s[i]:
                    count += 1
            print(s[i]+'('+str(count)+')')
