def main():
    L, Q = map(int, input().split())
    line = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            line.append(x)
        elif c == 2:
            line.sort()
            for j in range(len(line)):
                if line[j] == x:
                    print(line[j+1] - line[j])
                    break
