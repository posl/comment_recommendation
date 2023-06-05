def main():
    q = int(input())
    l = []
    for i in range(q):
        l.append(list(map(int,input().split())))
    bag = []
    for i in range(q):
        if l[i][0] == 1:
            bag.append(l[i][1])
        elif l[i][0] == 2:
            bag = [x+l[i][1] for x in bag]
        else:
            print(min(bag))
            bag.remove(min(bag))
