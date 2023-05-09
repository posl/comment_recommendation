def main():
    s = input()
    s = list(map(int, s))
    s.sort()
    ans = 0
    for i in range(1, 10):
        if i not in s:
            ans = i
    print(ans)

if __name__ == '__main__':
    main()