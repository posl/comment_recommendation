def main():
    s = input()
    t = input()
    count = 1000
    for i in range(len(s)-len(t)+1):
        tmp = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                tmp += 1
        count = min(tmp, count)
    print(count)

if __name__ == '__main__':
    main()