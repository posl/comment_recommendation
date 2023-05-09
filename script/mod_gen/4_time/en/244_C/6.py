def main():
    N = int(input())
    s = set()
    for i in range(1, 2*N+2):
        s.add(i)
    for i in range(1, N+1):
        print(i)
        s.remove(i)
        a = int(input())
        s.remove(a)
    print(s.pop())
    return 0

if __name__ == '__main__':
    main()