def main():
    N = int(input())
    if N < 250:
        print('0')
        return
    if N == 250:
        print('2')
        return
    N = N - 250
    N = N // 2
    N = N // 3
    print(N)
main()
