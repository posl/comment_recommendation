def main():
    count = int(input())
    for i in range(count):
        input()
        l = input().split()
        print(len([x for x in l if int(x) % 2 != 0]))
