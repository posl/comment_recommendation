def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    count = 0
    max_height = 0
    for h in h_list:
        if max_height <= h:
            max_height = h
            count += 1
    print(count)
