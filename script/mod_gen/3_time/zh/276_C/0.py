def exchange(perm):
    for i in range(len(perm)):
        if perm[i] > perm[i+1]:
            return i
    return -1

if __name__ == '__main__':
    exchange()