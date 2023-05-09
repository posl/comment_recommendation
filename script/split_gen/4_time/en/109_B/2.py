def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(1,n):
        if w[i] in w[:i]:
            print("No")
            return
        if w[i][0] != w[i-1][-1]:
            print("No")
            return
    print("Yes")
    return
