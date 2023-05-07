def main():
    A = list(map(int, input().split()))
    print('bust' if sum(A) >= 22 else 'win')

if __name__ == '__main__':
    main()