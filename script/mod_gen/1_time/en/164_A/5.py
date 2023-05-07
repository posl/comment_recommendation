def main():
    #input
    S, W = map(int, input().split())
    #output
    if S > W:
        print('safe')
    else:
        print('unsafe')

if __name__ == '__main__':
    main()