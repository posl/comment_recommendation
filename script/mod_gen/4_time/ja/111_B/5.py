def main():
    N = int(input())
    if N < 100 or N > 999:
        print('Error: 100 ≦ N ≦ 999')
        return
    if N % 111 == 0:
        print(N)
    else:
        print(((N // 111) + 1) * 111)

if __name__ == '__main__':
    main()