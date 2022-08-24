import paddle
import uvicorn as uvicorn
from LAC import LAC
from fastapi import FastAPI

paddle.enable_static()

# 批量样本输入, 输入为多个句子组成的list，平均速率更快
texts = [u"第一条 根据《中华人民共和国进出口商品检验法》(以下简称商检法)的规定，制定本条例。",
         u"建设单位隐瞒有关情况或者提供虚假材料申请施工许可证的，发证机关不予受理或者不予许可，并处1.8元以上三十万元以下罚款；构成犯罪的，依法追究刑事责任。"]
# lac_result = lac.run(texts)
# print(lac_result[1])
my_lac = LAC(model_path="my_lac_model")
# train_file = "./data/train.tsv"
# test_file = "./data/test.tsv"
# my_lac.train(model_save_dir='./my_lac_model/', train_data=train_file, test_data=test_file)
custom = "./data/custom.tsv"
# my_lac.load_customization(custom)
lac_result = my_lac.run(texts[1])
lac_result = dict(zip(lac_result[0], lac_result[1]))
print(lac_result)
