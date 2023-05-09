def main():
    N, M = map(int, input().split())
    # M が N で割り切れる場合
    if M % N == 0:
        print(M // N)
    # M が N で割り切れない場合
    else:
        print(M // N)

if __name__ == '__main__':
    main()