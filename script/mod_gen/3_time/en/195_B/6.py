def main():
    A,B,W = map(int,input().split())
    W *= 1000
    min_orange = W//B
    max_orange = W//A
    if W%B != 0:
        min_orange += 1
    if min_orange <= max_orange:
        print(min_orange,max_orange)
    else:
        print("UNSATISFIABLE")
main()

if __name__ == '__main__':
    main()