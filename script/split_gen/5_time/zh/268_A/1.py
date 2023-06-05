def main():
    a,b,c,d,e = map(int,input().split())
    arr = [a,b,c,d,e]
    arr.sort()
    count = 1
    for i in range(1,5):
        if arr[i] != arr[i-1]:
            count += 1
    print(count)
