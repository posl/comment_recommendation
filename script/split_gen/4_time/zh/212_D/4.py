def main():
    n = int(input())
    q = [int(input()) for i in range(n)]
    s = []
    for i in range(n):
        if q[i] == 3:
            print(s[0])
            del s[0]
        else:
            if q[i] == 1:
                s.append(q[i+1])
            else:
                s = [j+q[i+1] for j in s]
