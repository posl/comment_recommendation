def main():
    Q = int(input())
    cylinder = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            cylinder += [query[1]] * query[2]
        else:
            print(sum(cylinder[:query[1]]))
            cylinder = cylinder[query[1]:]
