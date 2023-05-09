def main():
    H, N = map(int, input().split())
    A = map(int, input().split())
    print('Yes' if H <= sum(A) else 'No')

if __name__ == '__main__':
    main()