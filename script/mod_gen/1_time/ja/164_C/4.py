def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    print(len(set(s)))

if __name__ == '__main__':
    main()