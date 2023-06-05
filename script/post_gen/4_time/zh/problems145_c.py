Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

=======
Suggestion 2

def get_distance(town_a,town_b):
    return ((town_a[0]-town_b[0])**2+(town_a[1]-town_b[1])**2)**(1/2)

=======
Suggestion 3

def calc_distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 4

def get_average_length(N, cities):
    import math
    import itertools
    total_length = 0
    num_of_paths = 0
    for path in itertools.permutations(cities):
        num_of_paths += 1
        for i in range(N-1):
            total_length += math.sqrt((path[i][0] - path[i+1][0])**2 + (path[i][1] - path[i+1][1])**2)
    return total_length/num_of_paths

=======
Suggestion 5

def get_distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 8

def main():
    print("")
