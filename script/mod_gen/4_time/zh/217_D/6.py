def cut_wood(wood, mark):
    wood.sort()
    wood.append(mark)
    wood.append(0)
    wood.append(mark)
    wood.sort()
    return wood

if __name__ == '__main__':
    cut_wood()