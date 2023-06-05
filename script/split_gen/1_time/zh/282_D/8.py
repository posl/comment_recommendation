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
