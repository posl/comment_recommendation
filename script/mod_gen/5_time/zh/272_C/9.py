def findEvenSum(list):
    evenSum = -1
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if (list[i]+list[j])%2==0:
                if evenSum<list[i]+list[j]:
                    evenSum = list[i]+list[j]
    return evenSum

if __name__ == '__main__':
    findEvenSum()