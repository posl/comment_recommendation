def main():
    n, k = map(int, input().split())
    foods = list(map(int, input().split()))
    hate_foods = list(map(int, input().split()))
    foods.sort()
    hate_foods.sort()
    for i in range(k):
        if foods[n-1] == hate_foods[i]:
            print("No")
            exit()
    print("Yes")
