def main():
    N = int(input())
    S, T = input().split()
    print(''.join([s+t for s,t in zip(S,T)]))

if __name__ == '__main__':
    main()