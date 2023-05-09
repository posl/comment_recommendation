def main():
    n = int(input())
    if n < 42:
        print(f'AGC0{n}')
    else:
        print(f'AGC{n+1}')

if __name__ == '__main__':
    main()