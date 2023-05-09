def shiritori():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    for i in range(n):
        if w[i] in w[i+1:]:
            return "No"
        if i != n-1 and w[i][-1] != w[i+1][0]:
            return "No"
    return "Yes"
print(shiritori())

if __name__ == '__main__':
    shiritori()