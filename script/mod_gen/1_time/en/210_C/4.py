def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    print(len(set(c[:K])))

if __name__ == '__main__':
    main()