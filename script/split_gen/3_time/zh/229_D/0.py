def main():
    s = input()
    k = int(input())
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] == '.':
            count += 1
        else:
            if max < count:
                max = count
            count = 0
    if max < count:
        max = count
    if max > k:
        print(max-k)
    else:
        print(0)
