def main():
    A,B,W = map(int,input().split())
    W *= 1000
    min_oranges = W//B
    max_oranges = W//A
    if min_oranges*B < W:
        min_oranges += 1
    if max_oranges*A > W:
        max_oranges -= 1
    if min_oranges <= max_oranges:
        print(min_oranges,max_oranges)
    else:
        print("UNSATISFIABLE")
