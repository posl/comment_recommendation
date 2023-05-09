def main():
    n = int(input())
    q = [input().split() for _ in range(n)]
    s = []
    for i in range(n):
        if q[i][0] == '1':
            s.append(int(q[i][1]))
        elif q[i][0] == '2':
            x = int(q[i][1])
            c = int(q[i][2])
            for j in range(c):
                if x in s:
                    s.remove(x)
                else:
                    break
        elif q[i][0] == '3':
            print(max(s) - min(s))
