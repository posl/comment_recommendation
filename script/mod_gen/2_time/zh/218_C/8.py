def main():
    p = list(map(int, input().split()))
    ans = []
    for i in range(26):
        ans.append(chr(ord('a') + p[i] - 1))
    print(''.join(ans))

if __name__ == '__main__':
    main()