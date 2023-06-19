def main():
    s = input()
    n = len(s)
    count = 0
    for i in range(n):
        if i % 2 == 0:
            if s[i] == '1':
                count += 1
        else:
            if s[i] == '0':
                count += 1
    print(min(count, n - count))
