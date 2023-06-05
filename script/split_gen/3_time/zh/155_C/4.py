def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    max = 1
    count = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            count += 1
        else:
            count = 1
        if max < count:
            max = count
    count = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            count += 1
        else:
            count = 1
        if max == count:
            print(s[i])
