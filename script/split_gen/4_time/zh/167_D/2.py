def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    next_town = [1]
    next_town.append(a[0])
    for i in range(n):
        next_town.append(a[next_town[-1]-1])
    #print(next_town)
    next_town = next_town[1:]
    #print(next_town)
    #print(next_town.index(next_town[-1]))
    #print(next_town[next_town.index(next_town[-1])+1:])
    if k <= next_town.index(next_town[-1]):
        print(next_town[k])
    else:
        k = k - next_town.index(next_town[-1])
        k = k % len(next_town[next_town.index(next_town[-1])+1:])
        print(next_town[next_town.index(next_town[-1])+1:][k])
