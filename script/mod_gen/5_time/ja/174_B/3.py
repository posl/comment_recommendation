def main():
    n, d = map(int, input().split())
    print(len([1 for _ in range(n) if sum(map(lambda x: x**2, map(int, input().split()))) <= d**2]))

if __name__ == '__main__':
    main()