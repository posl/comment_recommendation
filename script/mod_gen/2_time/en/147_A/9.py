def main():
    #input
    A = list(map(int, input().split()))
    #output
    print('bust' if sum(A) >= 22 else 'win')

if __name__ == '__main__':
    main()