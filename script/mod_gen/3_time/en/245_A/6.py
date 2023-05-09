def main():
    #Get input
    a, b, c, d = map(int, input().split())
    #Convert to seconds
    takahashi = a*60 + b
    aoki = c*60 + d
    #Compare
    if takahashi < aoki:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()