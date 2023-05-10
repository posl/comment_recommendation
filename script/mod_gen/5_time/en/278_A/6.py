def main():
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    for i in range(k):
        a.append(a.pop(0))
    print ' '.join(map(str,a))

if __name__ == '__main__':
    main()