def main():
    A, B = map(int, input().split())
    odd = False
    for i in range(1, 4):
        if (A * B * i) % 2 == 1:
            odd = True
    if odd:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()