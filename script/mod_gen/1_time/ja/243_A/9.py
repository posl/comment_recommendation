def main():
    v,a,b,c = map(int, input().split())
    print("F" if v <= a else "M" if v <= a+b else "T")

if __name__ == '__main__':
    main()