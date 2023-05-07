def main():
    n, k = map(int, input().split())
    friends = []
    for i in range(n):
        a, b = map(int, input().split())
        friends.append((a, b))
    friends.sort(key=lambda x:x[0])
    for i in range(n):
        if k >= friends[i][0]:
            k += friends[i][1]
        else:
            break
    print(k)
