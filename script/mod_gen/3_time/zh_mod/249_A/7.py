def main():
    A,B,C,D,E,F,X = map(int, input().split())
    takahashi = 0
    aoki = 0
    for i in range(1,X+1):
        if i % (A+B) <= A and i % (A+B) != 0:
            takahashi += 1
        if i % (D+E) <= D and i % (D+E) != 0:
            aoki += 1
    if takahashi > aoki:
        print('Takahashi')

if __name__ == '__main__':
    main()