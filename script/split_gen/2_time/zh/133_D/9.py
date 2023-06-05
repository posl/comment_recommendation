def main():
    L,R = map(int, input().split())
    if R-L >= 2019:
        print(0)
        return
    else:
        min = 2019
        for i in range(L,R):
            for j in range(i+1,R+1):
                if (i*j)%2019 < min:
                    min = (i*j)%2019
                    if min == 0:
                        print(0)
                        return
        print(min)
        return
