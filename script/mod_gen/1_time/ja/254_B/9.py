def main():
    N = int(input())
    for i in range(N):
        #print(i)
        if i == 0:
            print(1)
        else:
            print(' '.join(map(str, a)))
        a = [1] * (i+1)
        for j in range(1, i):
            a[j] = a[j-1] + a[j]
main()

if __name__ == '__main__':
    main()