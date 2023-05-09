def main():
    n,m = map(int,input().split())
    b = []
    for i in range(n):
        b.append(list(map(int,input().split())))
    for i in range(10**8):
        if i*7 + 1 == b[0][0]:
            for j in range(n):
                for k in range(m):
                    if i*7 + k + 1 != b[j][k]:
                        return print("No")
            return print("Yes")
    return print("No")
