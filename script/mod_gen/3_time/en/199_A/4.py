def main():
    A,B,C = map(int, input().split())
    if A*A + B*B < C*C:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()