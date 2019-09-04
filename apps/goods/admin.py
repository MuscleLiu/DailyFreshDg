from django.contrib import admin
from django.core.cache import cache
from goods.models import GoodsType, IndexGoodsBanner, IndexTypeGoodsBanner,indexPromotionBanner,Goods, GoodSKU
# Register your models here.


class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """
          新增或者更新表中的数据时调用
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        super().save_model(request, obj, form, change)

        # 发出任务， 让 celery worker 重新生成首页静态页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清楚首页的缓存书记处
        cache.delete('index_page_data')

    def delete_model(self, request, obj):
        """
          删除表中的数据时调用
        :param request:
        :param obj:
        :return:
        """
        super().delete_model(request, obj)
        # 发出任务， 让 celery worker 重新生成首页静态页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清楚首页的缓存书记处
        cache.delete('index_page_data')

class GoodsTypeAdmin(BaseModelAdmin):
    pass

class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass

class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass

class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    pass

class GoodsSPUAdmin(BaseModelAdmin):
    pass

class GoodsSKUAdmin(BaseModelAdmin):
    pass

admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(indexPromotionBanner, IndexPromotionBannerAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmin)
admin.site.register(Goods, GoodsSPUAdmin)
admin.site.register(GoodSKU, GoodsSKUAdmin)