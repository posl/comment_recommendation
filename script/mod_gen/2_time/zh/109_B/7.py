def check_rule(w):
    for i in range(len(w)-1):
        if w[i] == w[i+1]:
            return False
    return True
n = int(input())
w = []
for i in range(n):
    w.append(input())
for i in range(n-1):
    if w[i] in w[i+1:] or w[i][-1] != w[i+1][0]:
        print("No")
        exit()
print("Yes")

if __name__ == '__main__':
    check_rule()