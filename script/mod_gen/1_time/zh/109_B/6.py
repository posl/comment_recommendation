def shiritori():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(1, n):
        if w[i-1][-1] != w[i][0]:
            return "No"
        if w.count(w[i]) > 1:
            return "No"
    return "Yes"
print(shiritori())
