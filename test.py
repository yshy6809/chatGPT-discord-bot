import re

text = '[1]: https://www.mafengwo.cn/cy/10065/ "北京美食,北京美食攻略,北京美食推荐 - 马蜂窝"\n[2]: https://www.dianping.com/beijing "北京美食_生活_团购_旅游_电影_优惠券 - 大众点评网"\n[3]: https://www.kempinski.com/cn/hotel-yansha-center "中国，北京，五星级酒店|北京燕莎中心凯宾斯基饭店"\n\n北京是一个美食之都，有很多好吃的饭店。根据网上的推荐[^1^][1] [^2^][2]，你可以试试以下几家：\n- 东来顺饭庄，是一家铜炉火锅的老字号，有多种口味的羊肉和各式小料，还有特色的炸酱面和爆肚。\n- 凯宾斯基饭店，是一家五星级酒店，有6间风格迥异的国际餐厅和酒吧，可以品尝到中西合璧的美食[^3^][3]。\n- 王府井小吃街，是一个集合了北京各地的特色小吃的地方，有糖葫芦、豆汁、炒肝、驴打滚等等，适合走走逛逛。\n'

def add_angle_brackets(match):
    return f"<{match.group(0)}>"

modified_text = re.sub(r'http[s]?://\S+', lambda x:f"<{x.group(0)}>", text)
print(modified_text)