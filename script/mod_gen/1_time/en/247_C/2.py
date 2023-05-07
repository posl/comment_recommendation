def main():
    n = int(input())
    s = '1'
    for i in range(2, n+1):
        s = s + ' ' + str(i) + ' ' + s
    print(s)

if __name__ == '__main__':
    main()