def get_representative(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = get_representative(parents[x])
        return parents[x]

if __name__ == '__main__':
    get_representative()