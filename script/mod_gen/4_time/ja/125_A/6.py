def main():
    A, B, T = map(int, input().split())
    print(int((T + 0.5)//A * B))

if __name__ == '__main__':
    main()