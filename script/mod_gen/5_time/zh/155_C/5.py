def main():
    n = int(input())
    s = {}
    for i in range(n):
        si = input()
        if si in s:
            s[si] += 1
        else:
            s[si] = 1
    max = 0
    for i in s:
        if s[i] > max:
            max = s[i]
    for i in sorted(s):
        if s[i] == max:
            print(i)

if __name__ == '__main__':
    main()