def main():
    s = input()
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    s = list(s)
    for i in range(q):
        t = query[i][0]
        k = query[i][1]
        if t % 3 == 0:
            if k % 3 == 1:
                print(s[0])
            elif k % 3 == 2:
                print(s[1])
            elif k % 3 == 0:
                print(s[2])
        elif t % 3 == 1:
            if k % 3 == 1:
                print(s[1])
            elif k % 3 == 2:
                print(s[2])
            elif k % 3 == 0:
                print(s[0])
        elif t % 3 == 2:
            if k % 3 == 1:
                print(s[2])
            elif k % 3 == 2:
                print(s[0])
            elif k % 3 == 0:
                print(s[1])
