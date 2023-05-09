def main():
    s, w = map(int, input().split())
    print('unsafe' if w >= s else 'safe')

if __name__ == '__main__':
    main()