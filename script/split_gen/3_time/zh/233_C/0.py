def main():
    n,x = map(int,input().split())
    bag = []
    for i in range(n):
        bag.append(list(map(int,input().split()))[1:])
    ans = 0
    for i in range(1,x+1):
        if x%i == 0:
            for j in range(n):
                if i in bag[j]:
                    break
            else:
                ans += 1
    print(ans)
