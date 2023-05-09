def main():
    #n = input()
    #a = int(input())
    #b, c = map(int, input().split())
    #s = input()
    #a = list(map(int, input().split()))
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = input().split()
    #a = [int(input()) for i in range(n)]
    #a = [int(input().split()) for i in range(n)]
    #a = [input().split() for i in range(n)]
    #a = [int(input()) for i in range(n)]
    #a = [int(input()) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    q = int(input())
    x = []
    for i in range(q):
        x.append(list(map(int, input().split())))
    bag = []
    for i in range(q):
        if x[i][0] == 1:
            bag.append(x[i][1])
        elif x[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += x[i][1]
        elif x[i][0] == 3:
            print(min(bag))
            bag.remove(min(bag))
