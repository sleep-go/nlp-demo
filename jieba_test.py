# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import jieba
import paddle


def print_hi():
    paddle.enable_static()
    # jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持
    strs = ["第一条　根据《中华人民共和国进出口商品检验法》(以下简称商检法)的规定，制定本条例。",
            "第二条　海关总署主管全国进出口商品检验工作。海关总署设在省、自治区、直辖市以及进出口商品的口岸、集散地的出入境检验检疫机构及其分支机构(以下简称出入境检验检疫机构)，管理所负责地区的进出口商品检验工作。",
            "第三条　海关总署应当依照商检法第四条规定，制定、调整必须实施检验的进出口商品目录(以下简称目录)并公布实施。"]
    for str in strs:
        seg_list = jieba.cut(str, use_paddle=True)  # 使用paddle模式
        print("Paddle Mode: " + '/'.join(list(seg_list)))

    seg_list = jieba.cut(strs[0], cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式

    seg_list = jieba.cut(strs[0], cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

    seg_list = jieba.cut(strs[0])  # 默认是精确模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
