def main():
    n = int(input())
    w = [input() for _ in range(n)]
    #print(n)
    #print(w)
    for i in range(n):
        #print(i)
        if i == 0:
            pass
        else:
            if w[i-1][-1] != w[i][0]:
                print('No')
                return
            else:
                pass
        if w[i] in w[:i]:
            print('No')
            return
        else:
            pass
    print('Yes')

if __name__ == '__main__':
    main()