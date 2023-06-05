def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n):
        if i == 0:
            continue
        if w[i] in w[:i]:
            print("No")
            exit()
        if w[i][0] != w[i-1][-1]:
            print("No")
            exit()
    print("Yes")
