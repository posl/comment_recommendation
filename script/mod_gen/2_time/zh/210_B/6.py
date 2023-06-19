def main():
    # N = int(input())
    # S = input()
    N = 5
    S = '00101'
    for i in range(N):
        if S[i] == '1':
            if i % 2 == 0:
                print('高桥')
            else:
                print('青木')
            break

if __name__ == '__main__':
    main()