def main():
    n = int(input())
    bag = []
    for i in range(n):
        query = input()
        if query[0] == '1':
            bag.append(int(query[2:]))
        elif query[0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query[2:])
        elif query[0] == '3':
            print(min(bag))
            bag.remove(min(bag))
