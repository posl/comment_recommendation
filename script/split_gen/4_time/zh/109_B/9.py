def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    flag = True
    for j in range(n-1):
        if w[j][-1] != w[j+1][0]:
            flag = False
            break
        for k in range(j+1,n):
            if w[j] == w[k]:
                flag = False
                break
    if flag:
        print("Yes")
    else:
        print("No")
