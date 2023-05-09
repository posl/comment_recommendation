def main():
    n = int(input())
    cnt = 0
    for i in range(3, len(str(n))+1):
        for j in range(3**i):
            s = ''
            for k in range(i):
                if j%(3**(k+1))//3**k == 0:
                    s += '3'
                elif j%(3**(k+1))//3**k == 1:
                    s += '5'
                else:
                    s += '7'
            if int(s) <= n and len(set(s)) == 3:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()