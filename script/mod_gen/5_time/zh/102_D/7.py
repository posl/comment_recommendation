def split_list(list1):
    list2=[]
    for i in range(len(list1)):
        list2.append(sum(list1[:i+1]))
    return list2
N=int(input())
A=list(map(int,input().split()))
A1=split_list(A)
A1.sort()
A2=A1[::-1]
A3=A2[0]-A2[-1]
print(A3)

if __name__ == '__main__':
    split_list()