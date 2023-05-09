def main():
    n = int(input())
    array = []
    for i in range(n):
        array.append(input().split())
    #print(array)
    array2 = []
    for i in range(n):
        array2.append(array[i][1:])
    #print(array2)
    array3 = []
    for i in range(n):
        array3.append(''.join(array2[i]))
    #print(array3)
    array4 = []
    for i in range(n):
        array4.append(int(array3[i]))
    #print(array4)
    array5 = []
    for i in range(n):
        array5.append(array4.count(array4[i]))
    #print(array5)
    array6 = []
    for i in range(n):
        if array5[i] == 1:
            array6.append(1)
        else:
            array6.append(0)
    #print(array6)
    print(sum(array6))
