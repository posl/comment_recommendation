def main():
    N, K, A = map(int, raw_input().split())
    print (A + K - 1) % N + 1
main()

if __name__ == '__main__':
    main()