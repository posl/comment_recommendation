def solution(x,y,z):
    if y>z:
        return -1
    else:
        return abs(z-x)
x,y,z=map(int,input().split())
print(solution(x,y,z))
