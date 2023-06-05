def main():
    n = int(input())
    print(1)
    i = int(input())
    if i == 2:
        print(3)
    else:
        print(2)
    while True:
        i = int(input())
        if i == 0:
            break
        print(i+1)
        i = int(input())
        if i == 2:
            print(3)
        else:
            print(2)
    return
main()
