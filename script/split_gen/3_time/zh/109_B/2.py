def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n):
        if i != 0:
            if w[i - 1][-1] != w[i][0]:
                print("No")
                return
        if w.count(w[i]) > 1:
            print("No")
            return
    print("Yes")
    return
