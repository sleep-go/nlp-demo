from LAC import LAC

# 装载分词模型
lac = LAC(mode='seg')

# 单个样本输入，输入为Unicode编码的字符串
text = u"LAC是个优秀的分词工具"
seg_result = lac.run(text)
print(seg_result)
# 批量样本输入, 输入为多个句子组成的list，平均速率会更快
texts = [u"LAC是个优秀的分词工具", u"百度是一家高科技公司"]
seg_result = lac.run(texts)
print(seg_result)

# 装载LAC模型
lac = LAC(mode='lac', model_path="")
# 标签	含义	    标签	含义	    标签	    含义	    标签	    含义
# n	    普通名词	f	方位名词	s	    处所名词	nw	    作品名
# nz	其他专名	v	普通动词	vd	    动副词	vn	    名动词
# a	    形容词	ad	副形词	an	    名形词	d	    副词
# m 	数量词	q	量词	    r	    代词	    p	    介词
# c	    连词	    u	助词	    xc	    其他虚词	w	    标点符号
# PER	人名	    LOC	地名	O   RG	    机构名	TIME	时间

# 批量样本输入, 输入为多个句子组成的list，平均速率更快
texts = [u"第一条　根据《中华人民共和国进出口商品检验法》(以下简称商检法)的规定，制定本条例。",
         u"第二条　海关总署主管全国进出口商品检验工作。"]
lac_result = lac.run(texts)
print(lac_result[0])
print(lac_result[1])
