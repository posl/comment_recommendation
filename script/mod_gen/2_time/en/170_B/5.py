def animals(x, y):
    if x * 2 == y or x * 4 == y:
        return "Yes"
    if x * 2 > y:
        return "No"
    if (y - x * 2) % 2 == 0:
        return "Yes"
    return "No"

if __name__ == '__main__':
    animals()