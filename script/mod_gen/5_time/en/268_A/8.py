def main():
    a = input().split()
    a = list(dict.fromkeys(a))
    print(len(a))

if __name__ == '__main__':
    main()