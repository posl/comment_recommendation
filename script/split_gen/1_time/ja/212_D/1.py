def main():
    q = int(input())
    num = []
    add = 0
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            num.append(query[1] - add)
        elif query[0] == 2:
            add += query[1]
        else:
            print(min(num) + add)
            num.remove(min(num))
