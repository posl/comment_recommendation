def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if str(i).find('7') == -1 and oct(i).find('7') == -1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()