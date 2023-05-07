def find_parent(person, parents):
    if person == 1:
        return 0
    else:
        return 1 + find_parent(parents[person], parents)

if __name__ == '__main__':
    find_parent()