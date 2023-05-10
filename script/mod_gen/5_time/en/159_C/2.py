def main():
    l = int(input())
    print((l/3)**3 if l%3==0 else (l//3+1)*(l//3)*(l//3))

if __name__ == '__main__':
    main()