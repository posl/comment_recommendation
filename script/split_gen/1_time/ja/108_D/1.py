def main():
    L = int(input())
    ans = []
    ans.append([1,2,0])
    ans.append([2,3,0])
    ans.append([3,4,0])
    ans.append([1,5,0])
    ans.append([2,6,0])
    ans.append([3,7,0])
    ans.append([4,8,0])
    ans.append([5,6,1])
    ans.append([6,7,1])
    ans.append([7,8,1])
    for i in range(2,L):
        ans.append([i,i+3,i-1])
        ans.append([i+3,i+4,0])
    print(len(ans),len(ans))
    for a in ans:
        print(*a)
