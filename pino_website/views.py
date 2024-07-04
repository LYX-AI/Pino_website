from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
def index(request):
    print(request.user)
    return render(request, 'index.html')
    # 这使用模板加载器 loader 来获取 index.html 模板。它基本上是在告诉 Django 去项目的模板目录下查找名为 index.html 的文件
    # template=loader.get_template('index.html')
    # return HttpResponse(template.render({},request))
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')