def main():
    s = input()
    q = int(input())
    queries = [list(map(str, input().split())) for _ in range(q)]
    is_reverse = False
    for query in queries:
        if query[0] == '1':
            is_reverse = not is_reverse
        else:
            if (query[1] == '1' and not is_reverse) or (query[1] == '2' and is_reverse):
                s = query[2] + s
            else:
                s = s + query[2]
    if is_reverse:
        print(s[::-1])
    else:
        print(s)
