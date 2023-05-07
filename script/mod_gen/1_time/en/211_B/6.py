def main():
    #input
    S = [input() for _ in range(4)]
    #output
    if len(set(S)) == 4:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()