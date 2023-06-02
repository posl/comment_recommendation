#问题说明
#诗歌在线评委（POJ）是一个在线评委，给提交的字符串打分。
#有N次提交给POJ。  在最早的第i次提交中，提交了字符串S_i，并得到了T_i的分数。  (同一字符串可能被多次提交）。
#请注意，POJ不一定给相同字符串的提交物打相同的分数。
#如果提交的字符串从未在任何早期提交的作品中出现过，则该作品被认为是原创作品。
#如果一个提交物是原始提交物，且得分最高，则称其为最佳提交物。  如果有多个这样的提交，只有最早的一个被认为是最佳提交。
#找到最佳提交的索引。
#
#限制条件
#1 ≦ N ≦ 10^5
#S_i是一个由小写英文字符组成的字符串。
#S_i的长度在1到10之间，包括在内。
#0 ≦ T_i ≦ 10^9
#N和T_i是整数。
#
#输入
#输入来自标准输入，其格式如下：
#N
#S_1 T_1
#S_2 T_2
#.
#.
#.
#S_N T_N
#
#输出
#打印答案。
#
#输入样本1
#3
#aaa 10
#bbb 20
#aaa 30
#
#样本输出 1
#2
#我们将第i个最早的提交物称为提交物i。
#原始的提交物是提交物1和2。  提交的文件3不是原创的，因为它的字符串与提交的文件1相同。
#在原始提交的材料中，提交的材料2的分数最高。  因此，这是最好的作品。
#
#样本输入2
#5
#aaa 9
#bbb 10
#ccc 10
#ddd 10
#bbb 11
#
#样本输出2
#2
#原始提交的材料是提交的1，2，3，和4。
#其中，Submission 2, 3, 和4的分数最高。  在这种情况下，最早提交的材料，即提交材料2，是最好的。
#在这个例子中，请注意，如果多个原始提交物都有最高分，只有其中最早的一个被认为是最佳提交物。
#
#样本输入3
#10
#bb 3
#ba 1
#aa 4
#bb 1
#ba 5
#aa 9
#aa 2
#ab 6
#bb 5
#ab 3
#
#样本输出3
#8

def 