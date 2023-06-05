def main():
    N = int(input())
    s = set()
    for i in range(N):
        s.add(input())
    print(len(s))

if __name__ == '__main__':
    main()