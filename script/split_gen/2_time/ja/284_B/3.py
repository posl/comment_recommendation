def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(len(list(filter(lambda x: x % 2 == 1, A))))
