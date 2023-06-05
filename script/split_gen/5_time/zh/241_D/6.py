def main():
    q = int(input())
    
    arr = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            arr.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            arr.sort(reverse=True)
            cnt = 0
            for j in range(len(arr)):
                if arr[j] <= x:
                    cnt += 1
                if cnt == k:
                    print(arr[j])
                    break
            else:
                print(-1)
        else:
            x = int(query[1])
            k = int(query[2])
            arr.sort()
            cnt = 0
            for j in range(len(arr)):
                if arr[j] >= x:
                    cnt += 1
                if cnt == k:
                    print(arr[j])
                    break
            else:
                print(-1)
