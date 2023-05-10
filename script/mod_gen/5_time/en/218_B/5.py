def main():
    p = list(map(int, input().split()))
    s = [chr(p[i] + 96) for i in range(len(p))]
    print(''.join(s))

if __name__ == '__main__':
    main()