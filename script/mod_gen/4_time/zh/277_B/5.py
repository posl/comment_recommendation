def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    if len(set(a)) == n:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()