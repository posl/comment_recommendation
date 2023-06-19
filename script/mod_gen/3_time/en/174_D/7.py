def solution():
    n = int(input())
    stones = input()
    red = stones.count('R')
    white = stones.count('W')
    if red == 0 or white == 0:
        print(0)
    elif red == white:
        print(red)
    else:
        print(1+abs(red-white)//2)
solution()
