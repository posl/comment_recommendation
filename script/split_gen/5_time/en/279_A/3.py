def main():
    s = input().strip()
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            count += i
    print(count)
