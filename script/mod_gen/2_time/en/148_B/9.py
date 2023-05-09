def main():
    N = int(input())
    S,T = input().split()
    print(''.join([x+y for x,y in zip(S,T)]))

if __name__ == '__main__':
    main()