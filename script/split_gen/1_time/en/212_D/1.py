def main():
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    bag = []
    for q in query:
        if q[0] == '1':
            bag.append(int(q[1]))
        elif q[0] == '2':
            for i in range(len(bag)):
                bag[i] += int(q[1])
        else:
            print(min(bag))
            bag.remove(min(bag))
