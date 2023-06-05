def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    #print(s)
    #print(s[0][2])
    #print(s[1][0])
    min = 10000
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                if i-1 >= 0:
                    if s[i-1][j] == '-':
                        if min > 1:
                            min = 1
                if i+1 < h:
                    if s[i+1][j] == '-':
                        if min > 1:
                            min = 1
                if j-1 >= 0:
                    if s[i][j-1] == '-':
                        if min > 1:
                            min = 1
                if j+1 < w:
                    if s[i][j+1] == '-':
                        if min > 1:
                            min = 1
    print(min)
