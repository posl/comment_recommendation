def main():
    p = list(map(int, input().split()))
    print(''.join(list(map(lambda x: chr(x + 96), p))))

if __name__ == '__main__':
    main()