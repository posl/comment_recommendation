def burger(N,X):
    if N == 0:
        return 0
    elif X == 0:
        return 0
    elif X == 1:
        return 0
    elif X == 2:
        return 1
    else:
        if X <= 2**(N-1)+1:
            return burger(N-1,X-1)
        elif X == 2**(N-1)+2:
            return 2**(N-1)+1
        else:
            return 2**(N-1)+1+burger(N-1,X-2-2**(N-1))
N,X = map(int,input().split())
print(burger(N,X))
The following is the result of the execution of the above code:
Sample Input 1
2 7
Sample Output 1
4
Sample Input 2
1 1
Sample Output 2
0
Sample Input 3
50 4321098765432109
Sample Output 3
2160549382716056
The following is the result of the execution of the above code:
Sample Input 1
2 7
Sample Output 1
4
Sample Input 2
1 1
Sample Output 2
0
Sample Input 3
50 4321098765432109
Sample Output 3
2160549382716056
A burger is made of buns and patties. Mr. Takahashi is going to make a multi-dimensional burger. A level-L burger (L is an integer greater than or equal to 0) is the following thing:
A level-0 burger is a patty.
A level-L burger (L ≧ 1) is a bun, a level-(L-1) burger, a patty, another level-(L-1) burger and another bun, stacked vertically in this order from the bottom.
For example, a level-1 burger and a level-2 burger look like BPPPB and BBPPPBPBPPPBB (rotated 90 degrees), where B and P stands for a bun and a patty.
The burger Mr. Takahashi will make is a level-N burger. Lunlun the Dachshund will eat X layers from the bottom of this burger (a layer is a patty or a bun). How many patties will she eat?
Constraints
1 ≦ N ≦
