def shiritori(n, w):
    for i in range(n-1):
        if w[i] == w[i+1] or w[i][-1] != w[i+1][0]:
            return "No"
    return "Yes"
n = int(input())
w = []
for _ in range(n):
    w.append(input())
print(shiritori(n, w))
