def main():
    p = list(map(int, input().split()))
    s = [chr(ord('a') + p[i] - 1) for i in range(26)]
    print(''.join(s))

if __name__ == '__main__':
    main()