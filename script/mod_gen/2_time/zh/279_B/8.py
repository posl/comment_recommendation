def main():
    s = input().strip()
    print(s.count('vv') + s.count('wv') * 2 + s.count('vw') * 2 + s.count('ww') * 3)

if __name__ == '__main__':
    main()