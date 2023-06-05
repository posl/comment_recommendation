def main():
    n = int(input())
    ab = []
    for i in range(n-1):
        ab.append(list(map(int, input().split())))
    ab.sort()
    #print(ab)
    a = [0] * n
    for i in range(n-1):
        a[ab[i][0]-1] += 1
    #print(a)
    for i in range(n-1):
        if a[ab[i][1]-1] == n-1:
            print("Yes")
            exit()
    print("No")
