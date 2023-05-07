def main():
    A,B,C,D = map(int,input().split())
    if A==C:
        if B<D:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A<C:
            print("Aoki")
        else:
            print("Takahashi")

if __name__ == '__main__':
    main()