def count_box(box):
    box_count = 0
    for i in range(len(box)):
        if box[i] == '#':
            box_count += 1
    return box_count

if __name__ == '__main__':
    count_box()