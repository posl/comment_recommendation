def main():
    num = int(input())
    lists = []
    for i in range(num):
        lists.append(input())
    lists.reverse()
    for i in lists:
        print(i)
