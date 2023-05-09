def problems284_b():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(len([x for x in a if x % 2 == 1]))

if __name__ == '__main__':
    problems284_b()