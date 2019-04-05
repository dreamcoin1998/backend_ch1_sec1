import json
import requests

def weather(cityname):
    key = '7a941f15ea6a0983a08e270b2a796fbf' # 聚合天气申请的key
    api = 'http://v.juhe.cn/weather/index' # 聚合天气接口
    params = 'format=2&cityname=%s&key=%s' % (cityname, key) # 请求参数，包括城市名称和key
    url = api + '?' + params # 组成请求链接
    response = requests.get(url=url) # 根据聚合天气API文档，get返回一个json文件,此时response是response对象
    json_data = json.loads(response.text) # response.text返回一个string对象，json.load()返回一个字典
    result = json_data.get('result') # 获取result所对应的value，详见聚合天气API文档https://www.juhe.cn/docs/api/id/39
    sk = result.get('sk') # 获取sk里面result所对应的value
    response = dict()
    response['temperature'] = sk.get('temp') # 获取温度
    response['wind_direction'] = sk.get('wind_direction') # 获取风向
    response['wind_strength'] = sk.get('wind_strength') # 获取风力
    response['humidity'] = sk.get('humidity') # 获取当前湿度
    response['time'] = sk.get('time') # 获取更新时间
    return response

if __name__ == '__main__':
    data = weather('深圳')