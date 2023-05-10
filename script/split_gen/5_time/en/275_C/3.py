def main():
    str_list = []
    for i in range(9):
        str_list.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if str_list[i][j] == '#':
                count += 1
    print(count)
