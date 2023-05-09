def main():
    N, K = map(int, input().split())
    print(len(str(N).encode('utf-8')) * 8 // int(math.log2(K)))
main()

if __name__ == '__main__':
    main()