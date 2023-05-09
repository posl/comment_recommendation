def main():
    s = input()
    count = 0
    for i in range(0, len(s)-1):
        if s[i] == 'v' and s[i+1] == 'v':
            count += 1
    print(count)
