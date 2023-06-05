def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        temp = input().split()
        a.append(int(temp[0]))
        b.append(int(temp[1]))
    if 1 in a or 1 in b:
        print("Yes")
    else:
        print("No")
