def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    count = 0
    i = 0
    while i < n-1:
        j = i + 1
        while j < n and s[i] == s[j]:
            count += 1
            j += 1
        i = j
    print(count)

if __name__ == '__main__':
    main()