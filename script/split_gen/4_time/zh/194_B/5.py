def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = input().split()
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    a.sort()
    b.sort()
    if a[-1] > b[-1]:
        print(a[-1])
    else:
        print(b[-1])
