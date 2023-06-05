def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n):
        if w.count(w[i]) > 1 or (i != 0 and w[i][0] != w[i - 1][-1]):
            print("No")
            exit()
    print("Yes")
