def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        count = 0
        for j in range(i):
            if s[i] == s[j]:
                count += 1
        if count == 0:
            print(s[i])
        else:
            print(s[i] + '(' + str(count) + ')')
    return 0
