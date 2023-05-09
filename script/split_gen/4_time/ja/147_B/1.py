def main():
    s = input()
    n = len(s)
    count = 0
    for i in range(int(n/2)):
        if s[i] != s[n-i-1]:
            count += 1
    print(count)
