def main():
    n = int(input())
    print(sum([n.count(str(i)+str(j))*n.count(str(j)+str(i)) for i in range(1,10) for j in range(1,10)]))
