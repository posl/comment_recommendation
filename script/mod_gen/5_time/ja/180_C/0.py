def main():
    N = int(input())
    l = []
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            l.append(i)
            if i != N//i:
                l.append(N//i)
    l.sort()
    for i in l:
        print(i)

if __name__ == '__main__':
    main()