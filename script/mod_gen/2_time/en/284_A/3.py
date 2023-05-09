def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    l.reverse()
    for i in l:
        print(i)

if __name__ == '__main__':
    main()