def main():
    r = int(input())
    print('ABC' if r < 1200 else 'ARC' if r < 2800 else 'AGC')

if __name__ == '__main__':
    main()