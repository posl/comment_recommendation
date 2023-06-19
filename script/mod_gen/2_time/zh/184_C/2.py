def main():
    r_1, c_1 = map(int, input().split())
    r_2, c_2 = map(int, input().split())
    if r_1 == r_2 and c_1 == c_2:
        print(0)
        return
    if abs(r_1 - r_2) + abs(c_1 - c_2) <= 3:
        print(1)
        return
    if r_1 + c_1 == r_2 + c_2:
        print(1)
        return
    if r_1 - c_1 == r_2 - c_2:
        print(1)
        return
    if (r_1 + c_1) % 2 == (r_2 + c_2) % 2:
        print(2)
        return
    if abs(r_1 - r_2) + abs(c_1 - c_2) <= 6:
        print(2)
        return
    if abs((r_1 + c_1) - (r_2 + c_2)) <= 3:
        print(2)
        return
    if abs((r_1 - c_1) - (r_2 - c_2)) <= 3:
        print(2)
        return
    print(3)

if __name__ == '__main__':
    main()