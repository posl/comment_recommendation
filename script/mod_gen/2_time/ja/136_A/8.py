def main():
    # A,B,C = 6,4,3
    A,B,C = map(int,input().split())
    if B + C <= A:
        print(C)
    else:
        print(C - (A - B))

if __name__ == '__main__':
    main()