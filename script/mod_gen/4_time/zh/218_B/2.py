def main():
    p = list(map(int, input().split()))
    s = [chr(96+p[i]) for i in range(26)]
    print(''.join(s))

if __name__ == '__main__':
    main()