def get_neighbours(i,j):
    neighbours = []
    neighbours.append((i-1,j-1))
    neighbours.append((i-1,j))
    neighbours.append((i,j-1))
    neighbours.append((i,j+1))
    neighbours.append((i+1,j))
    neighbours.append((i+1,j+1))
    return neighbours

if __name__ == '__main__':
    get_neighbours()