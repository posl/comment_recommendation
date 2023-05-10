def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(int(b))
    original = []
    for i in range(len(s)):
        if s[i] not in s[:i]:
            original.append(i)
    max = 0
    maxindex = 0
    for i in original:
        if t[i] > max:
            max = t[i]
            maxindex = i
    print(maxindex + 1)

if __name__ == '__main__':
    main()