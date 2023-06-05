def main():
    n = int(input())
    array = [int(x) for x in input().split()]
    max = array[0]
    for i in range(n):
        if array[i] > max:
            max = array[i]
        if array[i] < max - 1:
            print("No")
            return
    print("Yes")
