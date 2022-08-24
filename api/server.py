import jieba
import paddle
from LAC import LAC
from fastapi import FastAPI
from numpy.compat import unicode
from pydantic import BaseModel

paddle.enable_static()
app = FastAPI()


@app.get("/")
async def home():
    return {"msg": "index"}


@app.get("/train/{mode}")
async def train(mode: str):
    my_lac = LAC(mode=mode)
    # 指定训练集
    train_file = "../data/train_" + mode + ".tsv"
    model_dir = "../my_" + mode + "_model/"
    my_lac.train(model_save_dir=model_dir, train_data=train_file)
    return {"msg": "训练成功"}


# 批量样本输入, 输入为多个句子组成的list，平均速率更快
# texts = [u"第一条 根据《中华人民共和国进出口商品检验法》(以下简称商检法)的规定，制定本条例。",
# u"建设单位隐瞒有关情况或者提供虚假材料申请施工许可证的，发证机关不予受理或者不予许可，并处1.8元以上三十万元以下罚款；构成犯罪的，依法追究刑事责任。"]
class ExtractItem(BaseModel):
    text: str


@app.post("/extract")
async def extract(args: ExtractItem):
    my_lac = LAC(model_path="../my_lac_model")
    custom = "../data/custom.tsv"
    # 装载干预词典, sep参数表示词典文件采用的分隔符，为None时默认使用空格或制表符'\t'
    my_lac.load_customization(custom)
    # 文本必须转换成unicode格式
    lac_result = my_lac.run(unicode(args.text))
    lac_result = list(zip(lac_result[0], lac_result[1]))
    return {"code": 200, "data": lac_result}


@app.get('/jieba')
async def jieba_test():
    strs = ["第一条 根据《中华人民共和国进出口商品检验法》(以下简称商检法)的规定，制定本条例。",
            "第二条 海关总署主管全国进出口商品检验工作。海关总署设在省、自治区、直辖市以及进出口商品的口岸、集散地的出入境检验检疫机构及其分支机构(以下简称出入境检验检疫机构)，管理所负责地区的进出口商品检验工作。",
            "第三条 海关总署应当依照商检法第四条规定，制定、调整必须实施检验的进出口商品目录(以下简称目录)并公布实施。"]
    for str in strs:
        seg_list = jieba.cut(str, use_paddle=True)  # 使用paddle模式
        print("Paddle Mode: ", ' '.join(list(seg_list)).split())

    seg_list = jieba.lcut(strs[0], cut_all=True)
    print("Full Mode: ", seg_list)  # 全模式

    seg_list = jieba.lcut(strs[0], cut_all=False)
    print("Default Mode: ", seg_list)  # 精确模式

    seg_list = jieba.lcut(strs[0])  # 默认是精确模式
    print("默认是精确模式", seg_list)

    seg_list = jieba.lcut_for_search(strs[0])  # 搜索引擎模式
    print("搜索引擎模式:", seg_list)

    return {"code": 200, "data": seg_list}
