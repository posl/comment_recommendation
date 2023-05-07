def count_non_repeat(string, i):
    count = 0
    for j in range(i, len(string)):
        if string[j] != string[j+i]:
            count += 1
        else:
            break
    return count

if __name__ == '__main__':
    count_non_repeat()