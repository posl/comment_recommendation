def main():
    #N, M = map(int, input().split())
    #S = input().split()
    #T = input().split()
    N, M = 5, 3
    S = "tokyo kanda akiba okachi ueno".split()
    T = "tokyo akiba ueno".split()
    for s in S:
        if s in T:
            print("Yes")
        else:
            print("No")
