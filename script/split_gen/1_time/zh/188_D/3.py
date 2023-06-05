def main():
    N,C = map(int, input().split())
    #print(N,C)
    array = []
    for i in range(N):
        a,b,c = map(int, input().split())
        array.append([a,b,c])
    #print(array)
    array.sort()
    #print(array)
    result = 0
    for i in range(N):
        start = array[i][0]
        end = array[i][1]
        cost = array[i][2]
        if i == 0:
            result += cost
            prev = end
        else:
            if start == prev:
                result += cost
                prev = end
            else:
                if start - prev > C:
                    result += C
                    result += cost
                    prev = end
                else:
                    result += cost
                    prev = end
    print(result)
