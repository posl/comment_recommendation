def main():
    r_1, c_1 = map(int, input().split())
    r_2, c_2 = map(int, input().split())
    if r_1 == r_2 and c_1 == c_2:
        print(0)
        return
    if r_1 + c_1 == r_2 + c_2 or r_1 - c_1 == r_2 - c_2 or abs(r_1 - r_2) + abs(c_1 - c_2) <= 3:
        print(1)
        return
    if (r_1 + c_1) % 2 == (r_2 + c_2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i - j) % 2 == 0:
                continue
            if abs(i) + abs(j) <= 3:
                continue
            if r_1 + i + c_1 + j == r_2 + c_2 or r_1 + i - c_1 - j == r_2 - c_2 or abs(r_1 + i - r_2) + abs(c_1 + j - c_2) <= 3:
                print(2)
                return
    print(3)
    return
