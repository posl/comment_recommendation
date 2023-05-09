def main():
    #input
    A, B, C, D = map(int, input().split())
    #output
    if A*60+B < C*60+D:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()