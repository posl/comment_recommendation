def main():
    n = int(input())
    s = [input() for i in range(n)]
    s.sort()
    max = 0
    count = 1
    for i in range(1,n):
        if s[i] == s[i-1]:
            count += 1
        else:
            if max < count:
                max = count
            count = 1
    if max < count:
        max = count
    count = 1
    for i in range(1,n):
        if s[i] == s[i-1]:
            count += 1
        else:
            if max == count:
                print(s[i-1])
            count = 1
    if max == count:
        print(s[n-1])
