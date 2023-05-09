def main():
    A,B,C,D = map(int,input().split())
    ans = -1
    for i in range(1,100000+1):
        A += B
        if A <= C * D:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()