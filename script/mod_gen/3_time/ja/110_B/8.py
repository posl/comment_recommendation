def main():
    n, m, x, y = map(int, input().split())
    lst_x = list(map(int, input().split()))
    lst_y = list(map(int, input().split()))
    max_x = max(lst_x)
    min_y = min(lst_y)
    if max_x < min_y and x < min_y and min_y <= y:
        print("No War")
    else:
        print("War")
main()

if __name__ == '__main__':
    main()