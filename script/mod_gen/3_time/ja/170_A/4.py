def main():
    x_list = list(map(int, input().split()))
    for idx, x in enumerate(x_list):
        if x == 0:
            print(idx+1)
            break

if __name__ == '__main__':
    main()