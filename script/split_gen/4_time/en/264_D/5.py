def main():
    s = input()
    a = "atcoder"
    count = 0
    for i in range(len(s)):
        if s[i] != a[i]:
            count += 1
    print(count)
