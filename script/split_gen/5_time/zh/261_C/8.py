def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] not in s[:i]:
            print(s[i])
        else:
            j = 1
            while True:
                if s[i] + '(' + str(j) + ')' not in s[:i]:
                    print(s[i] + '(' + str(j) + ')')
                    break
                else:
                    j += 1
