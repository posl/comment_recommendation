def main():
    n = int(input())
    v = list(map(int, input().split()))
    v1 = []
    v2 = []
    for i in range(n):
        if i % 2 == 0:
            v1.append(v[i])
        else:
            v2.append(v[i])
    v1_count = {}
    v2_count = {}
    for i in range(len(v1)):
        if v1[i] in v1_count:
            v1_count[v1[i]] += 1
        else:
            v1_count[v1[i]] = 1
        if v2[i] in v2_count:
            v2_count[v2[i]] += 1
        else:
            v2_count[v2[i]] = 1
    v1_max = 0
    v1_max_key = 0
    for key in v1_count:
        if v1_max < v1_count[key]:
            v1_max = v1_count[key]
            v1_max_key = key
    v2_max = 0
    v2_max_key = 0
    for key in v2_count:
        if v2_max < v2_count[key]:
            v2_max = v2_count[key]
            v2_max_key = key
    if v1_max_key == v2_max_key:
        v1_max2 = 0
        v1_max2_key = 0
        for key in v1_count:
            if key != v1_max_key and v1_max2 < v1_count[key]:
                v1_max2 = v1_count[key]
                v1_max2_key = key
        v2_max2 = 0
        v2_max2_key = 0
        for key in v2_count:
            if key != v2_max_key and v2_max2 < v2_count[key]:
                v2_max2 = v2_count[key]
                v2_max2_key = key
        if v1_max2 + v2_max < v2_max2 + v1_max:
            v1_max = v1_max2
        else:
            v2_max = v2_max2
    print(n - v1_max - v2_max)

if __name__ == '__main__':
    main()