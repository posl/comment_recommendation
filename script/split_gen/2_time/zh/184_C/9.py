def main():
    input_list = []
    for i in range(2):
        input_list.append(list(map(int, input().split())))
    r1, c1 = input_list[0][0], input_list[0][1]
    r2, c2 = input_list[1][0], input_list[1][1]
    if r1 == r2 and c1 == c2:
        print(0)
        exit()
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        exit()
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        exit()
    print(2)
