Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                break
        else:
            c[i] = ''
    for j in range(w):
        for i in range(h):
            if c[i][j] == '#':
                break
        else:
            for i in range(h):
                c[i] = c[i][:j] + c[i][j+1:]
    for i in range(h):
        print(c[i])

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    l = []
    for i in range(h):
        l.append(input())
    for j in range(w):
        count = 0
        for i in range(h):
            if l[i][j] == '#':
                count += 1
        print(count)

=======
Suggestion 3

def solve(h, w, c):
    res = []
    for i in range(w):
        count = 0
        for j in range(h):
            if c[j][i] == '#':
                count += 1
        res.append(count)
    return res

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    for i in range(W):
        print(sum([1 for j in range(H) if C[j][i] == '#']))

=======
Suggestion 5

def problems274_b():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    for i in range(W):
        count = 0
        for j in range(H):
            if C[j][i] == '#':
                count += 1
        print(count)

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    c = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        c[i] = input()
    for i in range(w):
        x = 0
        for j in range(h):
            if c[j][i] == '#':
                x += 1
        print(x)

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    grid = [input() for i in range(h)]
    for i in range(w):
        print(sum([1 if grid[j][i] == '#' else 0 for j in range(h)]))

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    c = []
    for i in range(H):
        c.append(list(map(str, input().split())))
    for i in range(W):
        count = 0
        for j in range(H):
            if c[j][i] == '#':
                count += 1
        print(count, end = ' ')

=======
Suggestion 9

def get_input():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(input())

    return h, w, grid

=======
Suggestion 10

def main():
    # Take input from stdin
    input_str = input()
    input_arr = input_str.split(" ")
    H = int(input_arr[0])
    W = int(input_arr[1])
    #print("H = ", H, " W = ", W)
    #print("input_str = ", input_str)
    #print("input_arr = ", input_arr)
    #print("input_arr[0] = ", input_arr[0])
    #print("input_arr[1] = ", input_arr[1])
    #print("input_arr[2] = ", input_arr[2])
    #print("input_arr[3] = ", input_arr[3])
    #print("input_arr[4] = ", input_arr[4])
    #print("input_arr[5] = ", input_arr[5])
    #print("input_arr[6] = ", input_arr[6])
    #print("input_arr[7] = ", input_arr[7])
    #print("input_arr[8] = ", input_arr[8])
    #print("input_arr[9] = ", input_arr[9])
    #print("input_arr[10] = ", input_arr[10])
    #print("input_arr[11] = ", input_arr[11])
    #print("input_arr[12] = ", input_arr[12])
    #print("input_arr[13] = ", input_arr[13])
    #print("input_arr[14] = ", input_arr[14])
    #print("input_arr[15] = ", input_arr[15])
    #print("input_arr[16] = ", input_arr[16])
    #print("input_arr[17] = ", input_arr[17])
    #print("input_arr[18] = ", input_arr[18])
    #print("input_arr[19] = ", input_arr[19])
    #print("input_arr[20] = ", input_arr[20])
    #print("input_arr[21] = ", input_arr[21])
    #print("input_arr[22] = ", input_arr[22])
    #print("input_arr[23] = ", input_arr[23])
    #print("input_arr[24] = ", input_arr[24])
    #print("input_arr[25] = ", input_arr[25])
    #print("input
