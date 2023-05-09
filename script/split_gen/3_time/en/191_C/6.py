def main():
    #input
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    #print(s)
    #find the first black
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                start = [i, j]
                break
        else:
            continue
        break
    #find the next black
    def find_next_black(start, s):
        i = start[0]
        j = start[1]
        #print(i, j)
        if i > 0 and s[i-1][j] == "#":
            return [i-1, j]
        elif i < h-1 and s[i+1][j] == "#":
            return [i+1, j]
        elif j > 0 and s[i][j-1] == "#":
            return [i, j-1]
        else:
            return [i, j+1]
    #find the next black
    next = find_next_black(start, s)
    #print(next)
    #count the sides
    count = 1
    while next != start:
        next = find_next_black(next, s)
        #print(next)
        count += 1
    #output
    print(count)
