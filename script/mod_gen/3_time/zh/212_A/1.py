def main():
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        print("error")
    elif a == 0:
        print("silver")
    elif b == 0:
        print("gold")
    else:
        print("alloy")

if __name__ == '__main__':
    main()