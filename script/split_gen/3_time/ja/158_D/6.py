def main():
    s = input()
    q = int(input())
    query = [input().split() for _ in range(q)]
    reverse = 0
    head = ""
    tail = ""
    for q in query:
        if q[0] == "1":
            reverse = 1 - reverse
        elif q[0] == "2":
            if q[1] == "1":
                if reverse == 0:
                    head = q[2] + head
                else:
                    tail = tail + q[2]
            else:
                if reverse == 0:
                    tail = tail + q[2]
                else:
                    head = q[2] + head
    if reverse == 1:
        print(tail[::-1] + s + head[::-1])
    else:
        print(head + s + tail)
