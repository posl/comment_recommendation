def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N = sorted(N, reverse=True)
    if N[-1] == 0:
        print(0)
        return
    if sum(N) % 3 != 0:
        print(-1)
        return
    N = [str(i) for i in N]
    N = ''.join(N)
    print(len(N)-N.count('0'))

if __name__ == '__main__':
    main()