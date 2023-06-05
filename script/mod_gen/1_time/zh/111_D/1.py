def find_path(x, y):
    if x == 0 and y == 0:
        return ""
    if x > 0:
        return find_path(x-1, y) + "R"
    if x < 0:
        return find_path(x+1, y) + "L"
    if y > 0:
        return find_path(x, y-1) + "U"
    if y < 0:
        return find_path(x, y+1) + "D"

if __name__ == '__main__':
    find_path()