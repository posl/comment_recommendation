def main():
    N = int(input())
    a = set()
    for i in range(2, 100000):
        for j in range(2, 40):
            if i ** j <= N:
                a.add(i ** j)
            else:
                break
    print(N - len(a))

if __name__ == '__main__':
    main()