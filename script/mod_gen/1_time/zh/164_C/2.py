def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    print(len(list(set(a))))

if __name__ == '__main__':
    main()