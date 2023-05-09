def main():
    s = input()
    s = s + s
    n = len(s)
    m = n//2
    s_min = s
    s_max = s
    for i in range(n):
        s_min = min(s_min, s[i:i+m])
        s_max = max(s_max, s[i:i+m])
    print(s_min)
    print(s_max)

if __name__ == '__main__':
    main()