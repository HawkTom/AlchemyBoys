## “达观杯”文本智能处理挑战赛

#### 队伍名称：炼丹小分队

**成员：** 许涵博、童浩、张涛

#### 任务

建立模型通过长文本数据正文(article)，预测文本对应的类别(class)

#### **数据：** （达观官方数据百度网盘地址）

[点击下载](https://pan.baidu.com/s/13IMDPMz0rf8kM1JAea53uQ)   密码：y6m4

**train_set.csv** ：此数据集用于训练模型，每一行对应一篇文章。文章分别在“字”和“词”的级别上做了脱敏处理。共有四列： 第一列是文章的索引(id)，第二列是文章正文在“字”级别上的表示，即字符相隔正文(article)；第三列是在“词”级别上的表示，即词语相隔正文(word_seg)；第四列是这篇文章的标注(class)。 注：每一个数字对应一个“字”，或“词”，或“标点符号”。“字”的编号与“词”的编号是独立的！ 

**test_set.csv** ：此数据用于测试。数据格式同train_set.csv，但不包含class。 注：test_set与train_test中文章id的编号是独立的。 友情提示：请不要尝试用excel打开这些文件！由于一篇文章太长，excel可能无法完整地读入某一行！ 

#### 数据的预处理：

word2vec [向量词典数据](https://github.com/zhangtaochn/AlchemyBoys/tree/master/Data/result) 

TF-IDF

更新分享代码、相关论文等