def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    w_set = set(w)
    if len(w) != len(w_set):
        print('No')
        return
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()