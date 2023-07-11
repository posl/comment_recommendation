def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        if a[i][i] != '-':
            print('incorrect')
            return
        for j in range(i+1, n):

if __name__ == '__main__':
    main()