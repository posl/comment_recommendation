def main():
    r_1, c_1 = map(int, input().split())
    r_2, c_2 = map(int, input().split())
    if(r_1 == r_2 and c_1 == c_2):
        print(0)
    elif(r_1 + c_1 == r_2 + c_2 or r_1 - c_1 == r_2 - c_2 or abs(r_1 - r_2) + abs(c_1 - c_2) <= 3):
        print(1)
    elif((r_1 + c_1 + r_2 + c_2) % 2 == 0 or abs((r_1 + c_1) - (r_2 + c_2)) <= 3 or abs((r_1 - c_1) - (r_2 - c_2)) <= 3 or abs(r_1 - r_2) + abs(c_1 - c_2) <= 6):
        print(2)
    else:
        print(3)

if __name__ == '__main__':
    main()