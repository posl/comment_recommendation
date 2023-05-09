def main():
    A, B = map(int, input().split())
    print('{0:0.3f}'.format(round(B/A, 3)))

if __name__ == '__main__':
    main()