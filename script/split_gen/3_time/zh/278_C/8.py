def main():
    n, q = map(int, input().split())
    follow = []
    for i in range(q):
        follow.append(list(map(int, input().split())))
    for i in range(q):
        if follow[i][0] == 3:
            if follow[i][1] == follow[i][2]:
                print("Yes")
                continue
            if [follow[i][2], follow[i][1]] in follow:
                print("Yes")
            else:
                print("No")
