def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int,input().split())))
    ab.sort(key = lambda x:x[0])
    #print(ab)
    for i in range(n):
        if i == 0:
            min = ab[i][0]
            max = ab[i][1]
        else:
            if ab[i][0] >= min and ab[i][0] <= max:
                min = ab[i][0]
                if ab[i][1] < max:
                    max = ab[i][1]
            else:
                print(ab[i][0]-1)
                return
    print(max)
