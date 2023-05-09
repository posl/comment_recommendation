def main():
    p = list(map(int,input().split()))
    p = [chr(ord('a') + p[i] - 1) for i in range(26)]
    print(''.join(p))

if __name__ == '__main__':
    main()