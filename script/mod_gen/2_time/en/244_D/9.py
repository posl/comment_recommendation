def solve():
    s = input().split()
    t = input().split()
    if len(set(s)) == 1 and len(set(t)) == 1:
        print("Yes")
    elif len(set(s)) == 1 or len(set(t)) == 1:
        print("No")
    elif len(set(s)) == 2 and len(set(t)) == 2:
        print("Yes")
    else:
        print("No")
solve()
The problem statement says that the operation is repeated 10^18 times. However, it is not necessary to repeat the operation 10^18 times. It is sufficient to repeat the operation 3 times.
The operation is repeated 3 times. Thus, the color of the hat of Takahashi 1 is the same as the color of the hat of Takahashi 2 or the color of the hat of Takahashi 3. The color of the hat of Takahashi 2 is the same as the color of the hat of Takahashi 3. Thus, the color of the hat of Takahashi 1 is the same as the color of the hat of Takahashi 3. If the color of the hat of Takahashi 1 is different from the color of the hat of Takahashi 3, the color of the hat of Takahashi 2 is different from the color of the hat of Takahashi 3. Thus, the color of the hat of Takahashi 1 is the same as the color of the hat of Takahashi 2.
The color of the hat of Takahashi 1 is the same as the color of the hat of Takahashi 2. The color of the hat of Takahashi 1 is different from the color of the hat of Takahashi 3.
The color of the hat of Takahashi 1 is the same as the color of the hat of Takahashi 3. The color of the hat of Takahashi 1 is different from the color of the hat of Takahashi 2.
The color of the hat of Takahashi 1 is different from the color of the hat of Takahashi 2. The color of the hat of Takahashi 1 is different from the color of the hat of Takahashi 3. The color of the hat of Takahashi 2 is different from the color of the

if __name__ == '__main__':
    solve()