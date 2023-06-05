def main():
    edge = input()
    edge = edge.split()
    edge = list(map(int, edge))
    edge.sort()
    area = int(edge[0] * edge[1] / 2)
    print(area)

if __name__ == '__main__':
    main()