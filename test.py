from paddlenlp import Taskflow
import cv2

# seg = Taskflow("word_segmentation")
# res = seg("近日国家卫健委发布第九版新型冠状病毒肺炎诊疗方案")
# print(res)
#
# tag = Taskflow("pos_tagging")
# res = tag(
#     "建设单位隐瞒有关情况或者提供虚假材料申请施工许可证的，发证机关不予受理或者不予许可，并处1.8元以上三十万元以下罚款；构成犯罪的，依法追究刑事责任。")
#
# for i in range(0, len(res)):
#     print(list(res[i]))

from paddlenlp import Taskflow

# ner = Taskflow('ner')
# res = ner([
#     "建设单位隐瞒有关情况或者提供虚假材料申请施工许可证的，发证机关不予受理或者不予许可，并处1万元以上3万元以下罚款；构成犯罪的，依法追究刑事责任"])
# print(res)

nptag = Taskflow("knowledge_mining", model="nptag")
res = nptag(
    "建设单位隐瞒有关情况或者提供虚假材料申请施工许可证的，发证机关不予受理或者不予许可，并处1万元以上3万元以下罚款；构成犯罪的，依法追究刑事责任")
print(res)

wordtag_ie = Taskflow("knowledge_mining", with_ie=True)
res = wordtag_ie(
    "建设单位隐瞒有关情况或者提供虚假材料申请施工许可证的，发证机关不予受理或者不予许可，并处1万元以上3万元以下罚款；构成犯罪的，依法追究刑事责任")
print(res)
