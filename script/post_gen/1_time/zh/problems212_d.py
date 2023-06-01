Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    query = []
    result = []
    for i in range(N):
        query.append(list(map(int, input().split())))
    bag = []
    for i in range(N):
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += query[i][1]
        elif query[i][0] == 3:
            result.append(min(bag))
            bag.remove(min(bag))
    for i in range(len(result)):
        print(result[i])

=======
Suggestion 2

def main():
    q = int(input())
    queue = []
    for i in range(q):
        query = input()
        if query[0] == '1':
            queue.append(int(query.split()[1]))
        elif query[0] == '2':
            queue = [x + int(query.split()[1]) for x in queue]
        else:
            print(min(queue))
            queue.remove(min(queue))

=======
Suggestion 3

def main():
    q = int(input())
    x = []
    for i in range(q):
        x.append(list(map(int,input().split())))
    x = x[::-1]
    bag = []
    for i in range(q):
        if x[i][0] == 1:
            bag.append(x[i][1])
        elif x[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += x[i][1]
        else:
            print(bag.pop(bag.index(min(bag))))

=======
Suggestion 4

def main():
    Q = int(input())
    bag = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            bag = [x + int(query[1]) for x in bag]
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 5

def main():
    n = int(input())
    query = []
    for i in range(n):
        query.append(list(map(int, input().split())))
    query.reverse()
    bag = []
    for i in range(n):
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += query[i][1]
        elif query[i][0] == 3:
            print(bag.pop(bag.index(min(bag))))

=======
Suggestion 6

def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append(input())
    for i in range(n):
        if list[i][0] == '1':
            list[i] = list[i].split()
            list[i] = int(list[i][1])
        elif list[i][0] == '2':
            list[i] = list[i].split()
            list[i] = int(list[i][1])
        else:
            list[i] = int(list[i])
    list1 = []
    for i in range(n):
        if list[i] == 3:
            list1.append(i)
    list2 = []
    for i in range(len(list1)):
        for j in range(list1[i]):
            if list[j] == 3:
                list2.append(j)
    list3 = []
    for i in range(len(list2)):
        list4 = []
        for j in range(list2[i], list1[i]):
            list4.append(list[j])
        list3.append(list4)
    list5 = []
    for i in range(len(list3)):
        list5.append(min(list3[i]))
    for i in range(len(list5)):
        print(list5[i])

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    q = int(input())
    bag = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query[1])
        elif query[0] == '3':
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def main():
    q = int(input())
    bag = []
    for i in range(q):
        p, x = input().split()
        if p == '1':
            bag.append(int(x))
        elif p == '2':
            bag = [b+int(x) for b in bag]
        else:
            print(min(bag))
            bag.remove(min(bag))
