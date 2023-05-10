def main():
    h, w, rs, cs = map(int, input().split())
    n = int(input())
    walls = set()
    for i in range(n):
        r, c = map(int, input().split())
        walls.add((r, c))
    q = int(input())
    moves = []
    for i in range(q):
        d, l = input().split()
        l = int(l)
        moves.append((d, l))
    #print(h, w, rs, cs)
    #print(n)
    #print(walls)
    #print(q)
    #print(moves)
    #print("-----"

if __name__ == '__main__':
    main()