def main():
    A, B = map(int, input().split())
    K = (A + B) / 2
    if K.is_integer():
        print(int(K))
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()