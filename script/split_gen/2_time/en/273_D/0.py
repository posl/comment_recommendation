def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    walls = set()
    for _ in range(N):
        r, c = map(int, input().split())
        walls.add((r, c))
    Q = int(input())
    for _ in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for _ in range(l):
                if (r_s, c_s - 1) not in walls:
                    c_s -= 1
        elif d == 'R':
            for _ in range(l):
                if (r_s, c_s + 1) not in walls:
                    c_s += 1
        elif d == 'U':
            for _ in range(l):
                if (r_s - 1, c_s) not in walls:
                    r_s -= 1
        elif d == 'D':
            for _ in range(l):
                if (r_s + 1, c_s) not in walls:
                    r_s += 1
        print(r_s, c_s)
main()
I have a list of strings that I want to print in a specific order. For example, I have a list of strings that I want to print out in this order:
['A', 'B', 'C', 'D', 'E']
I want to print out the list in this order:
A
D
B
E
C
I have tried using the following code, but it does not work:
for i in range(0, len(myList), 2):
    print(myList[i])
    print(myList[i+1])
I have a list of strings that are in this order:
['A', 'B', 'C', 'D', 'E']
I want to print out the list in this order:
A
D
B
E
C
I have tried using the following code, but it does not work:
for i in range(0, len(myList), 2):
    print(myList[i])
    print(myList[i+1])
I have a list of strings that are in this order:
['A', 'B', 'C', 'D', 'E']
I want to print out the list in this order:
A
D
B
E
C
I have tried using the
