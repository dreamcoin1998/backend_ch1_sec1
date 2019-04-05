import json
from django.http import HttpResponse, JsonResponse, FileResponse
from thirdparty import juhe
from utils.response import CommonResponseMixin
from django.views import View


def helloworld(request):
    print('request method: ', request.method)
    print('request META: ', request.META)
    print('request cookies: ', request.COOKIES)
    print('request QueryDict: ', request.GET)
    # return HttpResponse(content='Hello Django Response', status=200)
    m = {
        'message' : 'Hello Django Response'
    }
    return JsonResponse(data=m, safe=True, status=200)
    pass


class WeatherView(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        data = []
        receive_body = request.body.decode('utf-8')  # 请求体,以utf-8解码
        receive_body = json.loads(receive_body)  # 返回一个dict对象
        print(receive_body)
        cities = receive_body.get('cities') # 请求体里面不止有一个城市
        for city in cities:
            result = juhe.weather(city.get('city')) # city.get('city')获取城市名，传入函数中，返回城市具体天气信息
            result['city_info'] = city # 返回前端传进来的城市信息
            data.append(result)
        response_data = self.wrap_json_response(data)
        return JsonResponse(data=response_data, status=200, safe=False)