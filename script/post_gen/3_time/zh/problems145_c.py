Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    print("Hello World!")
    return

=======
Suggestion 2

def cal_dist(start, end):
    return ((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2) ** 0.5

=======
Suggestion 3

def get_distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

=======
Suggestion 4

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

=======
Suggestion 5

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

n=int(input())
towns=[]
for i in range(n):
    towns.append(list(map(int,input().split())))

=======
Suggestion 6

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 7

def perm(l):
    if len(l) <= 1:
        yield l
    else:
        for i in range(len(l)):
            s = l[:i] + l[i+1:]
            for p in perm(s):
                yield l[i:i+1] + p
