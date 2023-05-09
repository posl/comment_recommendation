def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    max = 0
    count = 0
    for i in range(n):
        if i == 0:
            max = 1
            count = 1
        elif s[i] == s[i-1]:
            count += 1
            if max < count:
                max = count
                name = s[i]
        else:
            count = 1
    print(name)
