def get_input():
    n, m, k = map(int, input().split())
    friends = []
    blocks = []
    for i in range(m):
        friends.append(list(map(int, input().split())))
    for i in range(k):
        blocks.append(list(map(int, input().split())))
    return n, m, k, friends, blocks

if __name__ == '__main__':
    get_input()