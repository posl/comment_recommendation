def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(set(s)))

if __name__ == '__main__':
    main()