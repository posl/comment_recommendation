def main():
    n, x = map(int, input().split())
    friends = list(map(int, input().split()))
    friends[x-1] = 0
    for i in range(n):
        if friends[i] == x:
            friends[i] = 0
    print(len([i for i in friends if i != 0]))
