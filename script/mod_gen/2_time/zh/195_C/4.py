def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = w // b
    max = w // a
    if min * a > w or max * b < w:
        print("UNSATISFIABLE")
    else:
        print(min,max)

if __name__ == '__main__':
    main()