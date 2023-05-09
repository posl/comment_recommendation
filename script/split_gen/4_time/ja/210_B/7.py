def main():
    n = int(input())
    s = input()
    if n == 1:
        if s == '0':
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if s[0] == '0':
            print('Takahashi')
        else:
            print('Aoki')
main()
