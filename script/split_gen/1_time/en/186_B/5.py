def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    a_sum = sum([sum(i) for i in a])
    a_min = min([min(i) for i in a])
    print(a_sum - h*w*a_min)
