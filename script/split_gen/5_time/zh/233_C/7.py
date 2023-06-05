def main():
    n,x = map(int,input().split())
    bag = []
    for i in range(n):
        bag.append(list(map(int,input().split())))
    print(bag)
