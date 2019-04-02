import json
import requests

def weather(cityname):
    key = '7a941f15ea6a0983a08e270b2a796fbf'
    api = 'http://v.juhe.cn/weather/index'
    params = 'format=2&cityname=%s&key=%s' % (cityname, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url) # 根据聚合天气API文档，get返回一个json文件,此时response是response对象
    json_data = json.loads(response.text) # response.text返回一个string对象，json.load()返回一个字典
    print(json_data)
    result = json_data.get('result') # 获取result所对应的value，详见聚合天气API文档https://www.juhe.cn/docs/api/id/39
    sk = result.get('sk')
    response = dict()
    response['temperature'] = sk.get('temp')
    response['wind_direction'] = sk.get('wind_direction')
    response['wind_strength'] = sk.get('wind_strength')
    response['humidity'] = sk.get('humidity')
    response['time'] = sk.get('time')
    return response

if __name__ == '__main__':
    data = weather('深圳')