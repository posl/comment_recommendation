def main():
    A,B,W = map(int,input().split())
    W = W * 1000
    min = W // B
    max = W // A
    if W % B != 0:
        min += 1
    if W % A != 0:
        max -= 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min,max)

if __name__ == '__main__':
    main()