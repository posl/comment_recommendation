def main():
    l = int(input())
    print((l/3)**3 if l%3==0 else ((l-1)/3)**3 if l%3==1 else ((l-2)/3)**3)

if __name__ == '__main__':
    main()