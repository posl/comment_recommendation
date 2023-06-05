def main():
    L,Q = map(int,input().split())
    cut_point = [0,L]
    for i in range(Q):
        c_i,x_i = map(int,input().split())
        if c_i == 1:
            cut_point.append(x_i)
        if c_i == 2:
            cut_point.sort()
            index = cut_point.index(x_i)
            print(cut_point[index+1]-cut_point[index-1])
