def main():
    q = int(input())
    x = []
    for _ in range(q):
        x.append(list(map(int, input().split())))
    
    from collections import deque
    bag = deque()
    for i in range(q):
        if x[i][0] == 1:
            bag.append(x[i][1])
        elif x[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += x[i][1]
        else:
            print(bag.popleft())
