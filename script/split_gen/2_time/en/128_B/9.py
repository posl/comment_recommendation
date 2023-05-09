def main():
    N = int(input())
    rest_list = []
    for i in range(N):
        rest_list.append(input().split())
    rest_list.sort(key = lambda x: x[0])
    rest_list.sort(key = lambda x: int(x[1]), reverse = True)
    for i in range(N):
        print(rest_list[i][2])
