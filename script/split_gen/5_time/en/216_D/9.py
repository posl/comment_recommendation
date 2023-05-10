def main():
    N, M = map(int, input().split())
    cylinders = []
    for _ in range(M):
        cylinders.append(list(map(int, input().split()))[1:])
    cylinders.sort(key=lambda x:len(x))
    if len(cylinders[0]) == 2:
        print("Yes")
    else:
        print("No")
