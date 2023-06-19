def main():
    a,b,w = map(int, input().split())
    w *= 1000
    if w%a == 0:
        min = w//a
    else:
        min = w//a + 1
    if w%b == 0:
        max = w//b
    else:
        max = w//b
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)

if __name__ == '__main__':
    main()