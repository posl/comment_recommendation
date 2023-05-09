def main():
    L = int(input())
    if L % 3 == 0:
        print((L/3)**3)
    elif L % 3 == 1:
        print(((L-1)/3)**3 * 4)
    else:
        print(((L-2)/3)**3 * 8)

if __name__ == '__main__':
    main()