def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse = True) # 降順にソート
    if l[0] < sum(l[1:]):
        print("Yes")
    else:
        print("No")
