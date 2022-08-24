# jieba分词

`jieba_test.py`

~~~
支持全自动安装： 
easy_install jieba
或者
pip install jieba / pip3 install jieba
对于同一个句子，支持四种分词模式：
精确模式：试图将句子最精确地切开，适合文本分析。
全模式：把句子中所有的可以成词的词语都扫描出来, 速度非常快，但不能解决歧义。
搜索引擎模式：在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
paddle模式：利用PaddlePaddle深度学习框架，训练序列标注（双向GRU）网络模型实现分词。同时支持词性标注。paddle模式使用需安装paddlepaddle-tiny：
~~~

# 百度LAC

`lac_test.py`

```
# 标签	含义
# n	    普通名词
# f	    方位名词
# s	    处所名词
# nw    作品名
# nz	其他专名
# v	    普通动词
# vd    动副词
# vn    名动词
# a	    形容词
# ad	副形词
# an    名形词
# d	    副词
# m 	数量词
# q	    量词
# r	    代词
# p	    介词
# c	    连词
# u	    助词
# xc	其他虚词
# w	    标点符号
# PER	人名
# LOC	地名
# ORG   机构名
# TIME	时间
```

# TDengine

启动 TDengine

```shell
docker run -d -p 6030:6030 -p 6041:6041 -p 6043-6049:6043-6049 -p 6043-6049:6043-6049/udp tdengine/tdengine
```
