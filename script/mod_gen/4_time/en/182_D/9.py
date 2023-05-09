def sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum
n=int(input())
a=list(map(int,input().split()))
print(max([sum(a[:i+1]) for i in range(n)]))

if __name__ == '__main__':
    sum()