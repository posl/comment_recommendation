def main():
    n = int(input())
    snuke = 0
    takahashi = 0
    aoki = 0
    for i in range(n):
        name = input()
        if name == 'snuke':
            snuke += 1
        elif name == 'takahashi':
            takahashi += 1
        elif name == 'aoki':
            aoki += 1
    if snuke >= takahashi and snuke >= aoki:
        print('snuke')
    elif takahashi >= snuke and takahashi >= aoki:
        print('takahashi')
    elif aoki >= snuke and aoki >= takahashi:
        print('aoki')

if __name__ == '__main__':
    main()