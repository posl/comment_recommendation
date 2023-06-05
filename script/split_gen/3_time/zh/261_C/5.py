def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] not in s[:i]:
            print(s[i])
        else:
            count = 1
            while s[i] + "(" + str(count) + ")" in s[:i]:
                count += 1
            print(s[i] + "(" + str(count) + ")")
