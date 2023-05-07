def main():
    A,B,W = map(int,input().split())
    W *= 1000
    max = W//A
    min = W//B
    if W%B != 0:
        min += 1
    if max < min:
        print("UNSATISFIABLE")
    else:
        print(min,max)

if __name__ == '__main__':
    main()