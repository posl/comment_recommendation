def main():
    a,b,w = map(int,input().split())
    w = w * 1000
    if w%b == 0:
        min = w//b
    else:
        min = w//b + 1
    max = w//a
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)

if __name__ == '__main__':
    main()