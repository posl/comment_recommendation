def main():
    k = int(input())
    hour = 21 + k // 60
    minute = k % 60
    print(f'{hour:02d}:{minute:02d}')

if __name__ == '__main__':
    main()