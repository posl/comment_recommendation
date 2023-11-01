def main():
    A,B,C,D = map(int,input().split())
    if A*60+B < C*60+D:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()