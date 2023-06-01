Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, edges

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    u = []
    v = []
    for i in range(M):
        tmp = list(map(int, input().split()))
        u.append(tmp[0])
        v.append(tmp[1])
    #print(u)
    #print(v)
    #print(N, M)
    u_set = set(u)
    v_set = set(v)
    #print(u_set)
    #print(v_set)
    u_set = u_set & v_set
    #print(u_set)
    print(N*(N-1)//2 - M - len(u_set))

=======
Suggestion 3

def solve():
    n, m = map(int, input().split())
    lines = []
    for i in range(m):
        lines.append(list(map(int, input().split())))

    # print(n, m)
    # print(lines)

    # 1. 遍历所有边，找出所有不满足条件的边
    # 2. 去重
    # 3. 去除所有不满足条件的边，剩下的就是满足条件的边

    # 1. 遍历所有边，找出所有不满足条件的边
    # 1.1 遍历所有边，找出所有不满足条件的边
    # 1.2 去重
    # 1.3 去除所有不满足条件的边，剩下的就是满足条件的边
    # 1.1 遍历所有边，找出所有不满足条件的边
    # 1.2 去重
    # 1.3 去除所有不满足条件的边，剩下的就是满足条件的边
    # 1.1 遍历所有边，找出所有不满足条件的边
    # 1.2 去重
    # 1.3 去除所有不满足条件的边，剩下的就是满足条件的边
    # 1.1 遍历所有边，找出所有不满足条件的边
    # 1.2 去重
    # 1.3 去除所有不满足条件的边，剩下的就是满足条件的边
    # 1.1 遍历所有边，找出所有不满足条件的边
    # 1.2 去重
    # 1.3 去除所有不满足条件的边

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    edges.sort()
    ans = 0
    for i in range(m):
        u, v = edges[i]
        if i == 0 or edges[i - 1] != (u, v):
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print(type(n), type(m))
    i = 0
    j = 0
    list1 = []
    list2 = []
    while i < m:
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        list1.append(u)
        list2.append(v)
        i += 1
    #print(list1)
    #print(list2)
    i = 0
    j = 0
    list3 = []
    list4 = []
    while i < m:
        j = 0
        while j < m:
            if list1[i] != list1[j] and list1[i] != list2[j] and list2[i] != list1[j] and list2[i] != list2[j]:
                if list1[i] < list1[j]:
                    list3.append(list1[i])
                    list4.append(list1[j])
                elif list1[i] > list1[j]:
                    list3.append(list1[j])
                    list4.append(list1[i])
                if list1[i] < list2[j]:
                    list3.append(list1[i])
                    list4.append(list2[j])
                elif list1[i] > list2[j]:
                    list3.append(list2[j])
                    list4.append(list1[i])
                if list2[i] < list1[j]:
                    list3.append(list2[i])
                    list4.append(list1[j])
                elif list2[i] > list1[j]:
                    list3.append(list1[j])
                    list4.append(list2[i])
                if list2[i] < list2[j]:
                    list3.append(list2[i])
                    list4.append(list2[j])
                elif list2[i] > list2[j]:
                    list3.append(list2[j])
                    list4.append(list2[i])
            j += 1
        i += 1
    #print(list3)
    #print(list4)
    i = 0
    j = 0
    count = 0
    while i < len(list3):
        j = 0
        while j < len(list1):
            if list3[i]

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edge = list(map(int, input().split()))
        edges.append(edge)

    ans = 0
    for i in range(m):
        for j in range(i+1, m):
            if edges[i][0] != edges[j][0] and edges[i][0] != edges[j][1] and edges[i][1] != edges[j][0] and edges[i][1] != edges[j][1]:
                ans += 1

    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    u = []
    v = []
    for i in range(m):
        u_, v_ = map(int, input().split())
        u.append(u_)
        v.append(v_)
    print(n, m)
    print(u)
    print(v)

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    # 顶点
    vertexs = [0] * n
    # 边
    edges = [0] * m
    # 边关系
    edges_relation = [0] * m
    # 边关系的反向
    edges_relation_reverse = [0] * m
    # 边关系的反向
    edges_relation_reverse = [0] * m
    # 边关系的反向
    edges_relation_reverse = [0] * m

    # 建立顶点关系
    for i in range(m):
        # 顶点
        u, v = map(int, input().split())
        edges[i] = [u, v]
        edges_relation[i] = [u-1, v-1]
        edges_relation_reverse[i] = [v-1, u-1]

        vertexs[u-1] += 1
        vertexs[v-1] += 1

    # print(vertexs)
    # print(edges)
    # print(edges_relation)
    # print(edges_relation_reverse)

    # 建立边关系
    edges_relation_dict = {}
    edges_relation_reverse_dict = {}
    for i in range(m):
        # 顶点
        u, v = edges[i]
        if u > v:
            u, v = v, u
        edges_relation_dict.setdefault(u, {})
        edges_relation_dict[u].setdefault(v, 1)
        edges_relation_reverse_dict.setdefault(v, {})
        edges_relation_reverse_dict[v].setdefault(u, 1)

    # print(edges_relation_dict)
    # print(edges_relation_reverse_dict)

    # 顶点关系
    vertexs_relation = {}
    vertexs_relation_reverse = {}
    for i in range(n):
        vertexs_relation.setdefault(i, vertexs[i])
        vertexs_relation_reverse.setdefault(i, vertexs[i])

    # print(vertexs_relation)
    # print(vertexs_relation_reverse)

    # 判断是否存在边关系
    def exist_edge_relation(u, v):
        if u > v:
            u, v = v, u
        if v in edges_relation_dict.get(u, {}):
            return True
        return False

    # 判断是否存在反向
