def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append(input())
    for i in range(n):
        print(list[n-i-1])
