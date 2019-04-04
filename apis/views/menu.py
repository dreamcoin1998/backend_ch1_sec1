import os
import yaml
from backend_ch1_sec1 import settings
from django.http import JsonResponse
import utils.response

def init_app_data():
    data_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(data_file, 'r', encoding='utf-8') as f:
        apps = yaml.load(f) # 返回一个字典对象
        return apps

def get_menu(request):
    global_app_data = init_app_data()
    published_app_data = global_app_data.get('published')
    response = utils.response.wrap_json_response(data=published_app_data,code=utils.response.ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)