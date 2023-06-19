def shiritori():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n-1):
        if w[i][-1] != w[i+1][0]:
            return 'No'
        elif w.count(w[i]) > 1:
            return 'No'
    return 'Yes'
print(shiritori())
