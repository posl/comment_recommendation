def main():
    q = int(input())
    bag = []
    for i in range(q):
        p, x = input().split()
        if p == '1':
            bag.append(int(x))
        elif p == '2':
            bag = [b+int(x) for b in bag]
        else:
            print(min(bag))
            bag.remove(min(bag))
