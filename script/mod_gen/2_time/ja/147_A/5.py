def main():
    numbers = list(map(int, input().split()))
    if sum(numbers) >= 22:
        print('bust')
    else:
        print('win')

if __name__ == '__main__':
    main()