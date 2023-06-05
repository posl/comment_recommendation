def problem210_b():
    n = int(input())
    s = input()
    if s.find('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')
