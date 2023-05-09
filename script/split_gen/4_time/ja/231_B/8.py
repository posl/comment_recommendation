def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s.append('')
    max = 0
    maxs = ''
    count = 1
    for i in range(n):
        if s[i] == s[i + 1]:
            count += 1
        else:
            if max < count:
                max = count
                maxs = s[i]
            count = 1
    print(maxs)
