def main():
    A, B = map(float, input().split())
    print('{:.3f}'.format(round(B/A, 3)))

if __name__ == '__main__':
    main()