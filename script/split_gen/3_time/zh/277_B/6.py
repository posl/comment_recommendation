def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    l2 = []
    for i in l:
        if i not in l2:
            l2.append(i)
    if len(l) == len(l2):
        print("Yes")
    else:
        print("No")
