# 定义索引类
from haystack import indexes

# 导入你的模型类
from goods.models import GoodSKU

# 指定对于某个类的某些数据建立索引
# 索引类名格式： 模型类名 + Index
class GoodSKUIndex(indexes.SearchIndex, indexes.Indexable):
    """
      GoodSKU 建立索引
    """
    # 索引字段： use_template 指定根据表中的哪些字段建立索引文件，把说明放在一个文件中
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        # 返回模型类
        return GoodSKU

    # 建立索引数据
    def index_queryset(self, using=None):
        # 以下是对这个表里的所有字段建立索引
        return self.get_model().objects.all()