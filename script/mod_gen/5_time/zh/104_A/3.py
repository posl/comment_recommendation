def main():
    score = int(input())
    if score < 1200:
        print('ABC')
    elif score < 2800:
        print('ARC')
    else:
        print('AGC')

if __name__ == '__main__':
    main()