def main():
    s = input()
    q = int(input())
    t = []
    for i in range(q):
        t.append(input().split())
    head = ''
    tail = ''
    for i in range(q):
        if t[i][0] == '1':
            if head == '':
                head = s
            else:
                head, tail = tail, head
        else:
            if t[i][1] == '1':
                head = t[i][2] + head
            else:
                tail += t[i][2]
    if head == '':
        print(s + tail)
    else:
        print(head + s + tail)
