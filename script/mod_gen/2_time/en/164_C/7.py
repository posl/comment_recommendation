def main():
    N = int(input())
    print(len(set([input() for _ in range(N)])))

if __name__ == '__main__':
    main()