def main():
    n,k = [int(i) for i in input().split()]
    h = [int(i) for i in input().split()]
    count = 0
    for i in h:
        if i >= k:
            count += 1
    print(count)
