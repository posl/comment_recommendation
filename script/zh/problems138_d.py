#问题陈述
#给出的是一棵有N个顶点的有根树，编号为1到N。
#根是顶点1，第i条边（1 ≦ i ≦ N - 1）连接着顶点a_i和b_i。
#每个顶点都安装有一个计数器。最初，所有顶点的计数器的值都是0。
#现在，将进行以下Q操作：
#操作j（1 ≦ j ≦ Q）：用x_j增加根在顶点p_j的子树中包含的每个顶点上的计数器。
#找到所有操作后每个顶点上的计数器的值。
#
#限制条件
#2 ≦ N ≦ 2 × 10^5
#1 ≦ Q ≦ 2 × 10^5
#1 ≦ a_i < b_i ≦ N
#1 ≦ p_j ≦ N
#1 ≦ x_j ≦ 10^4
#给定的图是一棵树。
#输入的所有数值都是整数。
#
#输入
#输入是由标准输入提供的，格式如下：
#N Q
#a_1 b_1
#:
#a_{N-1} b_{N-1}
#p_1 x_1
#:
#p_Q x_Q
#
#输出
#打印顶点1，2，...，N上的计数器的值，在所有操作之后，按这个顺序，中间有空格。
#
#输入样本 1
#4 3
#1 2
#2 3
#2 4
#2 10
#1 100
#3 1
#
#样本输出1
#100 110 111 110
#这个输入中的树是这样的：
#每个操作都会改变顶点上的计数器的值，如下所示：
#操作1：将以顶点2为根的子树中的每个顶点的计数器增加10，即顶点2、3、4。现在顶点1、2、3、4上的计数器的值分别为0、10、10、10。
#操作2：将根植于顶点1的子树上的每个顶点的计数器增加100，即顶点1、2、3、4。现在顶点1、2、3、4的计数器的值分别为100、110、110、110。
#操作3：将根植于顶点3的子树上的每个顶点的计数器增加1，即顶点3。现在顶点1、2、3、4上的计数器的值分别为100、110、111、110。
#
#输入样本 2
#6 2
#1 2
#1 3
#2 4
#3 6
#2 5
#1 10
#1 10
#
#样本输出2
#20 20 20 20 20 20

def 