def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(str(input()))
    if len(w) != len(set(w)):
        print('No')
    else:
        for i in range(n-1):
            if w[i][-1] != w[i+1][0]:
                print('No')
                break
        else:
            print('Yes')

if __name__ == '__main__':
    main()