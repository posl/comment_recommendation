def main():
    p = list(map(int,input().split()))
    ans = []
    for i in p:
        ans.append(chr(96+i))
    print(''.join(ans))

if __name__ == '__main__':
    main()