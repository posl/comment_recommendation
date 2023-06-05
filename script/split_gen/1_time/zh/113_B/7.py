def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    temp = [t - x * 0.006 for x in h]
    print(temp.index(min(temp))+1)
