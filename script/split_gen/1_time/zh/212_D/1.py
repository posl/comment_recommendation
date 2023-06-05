def main():
    q = int(input())
    queue = []
    for i in range(q):
        query = input()
        if query[0] == '1':
            queue.append(int(query.split()[1]))
        elif query[0] == '2':
            queue = [x + int(query.split()[1]) for x in queue]
        else:
            print(min(queue))
            queue.remove(min(queue))
