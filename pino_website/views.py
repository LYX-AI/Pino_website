from django.http import HttpResponse
from django.template import loader
def index(request):
    # 这使用模板加载器 loader 来获取 index.html 模板。它基本上是在告诉 Django 去项目的模板目录下查找名为 index.html 的文件
    template=loader.get_template('index.html')
    return HttpResponse(template.render({},request))