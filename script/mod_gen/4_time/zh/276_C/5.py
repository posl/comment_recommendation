def is_sorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

if __name__ == '__main__':
    is_sorted()