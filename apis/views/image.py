from django.http import Http404, HttpResponse, FileResponse, JsonResponse
from backend_ch1_sec1 import settings
import os
import utils
from django.views import View
import hashlib
from utils.response import ReturnCode

def image(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5') # 解析get请求中的md5参数中的文件名
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg') # 图片资源在服务中存放的位置
        if not os.path.exists(imgfile):
            return Http404
        else:
            data = open(imgfile, 'rb').read()
            # return HttpResponse(content=data, content_type='image/png') # 如果不加content_type会直接以二进制流传输，无法分辨它的文件类型
            return FileResponse(open(imgfile, 'rb'), content_type='image/png')


class ImageView(View, utils.response.CommonResponseMixin): # 定义一个类视图，将会根据请求方式选择使用方法, 继承一个Mixin类
    def get(self, request):
        md5 = request.GET.get('md5')  # 解析get请求中的md5参数中的文件名
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')  # 图片资源在服务中存放的位置
        if  os.path.exists(imgfile):
            data = open(imgfile, 'rb').read()
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')
        else:
            response = self.wrap_json_response(code=ReturnCode.RESOURCE_NOT_FOUND)
            # return HttpResponse(content=data, content_type='image/png') # 如果不加content_type会直接以二进制流传输，无法分辨它的文件类型
            return JsonResponse(data=response, safe=False)

    def post(self, request):
        file = request.FILES
        response = []
        for key, value in file.items():
            content = value.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
            with open(path, 'wb') as f:
                f.write(content)
            response.append({
                "name": key,
                "md5": md5
            })
        message = 'post method success.'
        # response = utils.response.wrap_json_response(message=message)
        response = self.wrap_json_response(data=response, code=ReturnCode.SUCCESS) # 通过类方法直接调用wrap_json_response方法，不需要再进行导入
        return JsonResponse(data=response,safe=False)

    def put(self, request):
        message = 'put method success.'
        # response = utils.response.wrap_json_response(message=message)
        response = self.wrap_json_response(message=message)
        return JsonResponse(data=response,safe=False)

    def delete(self, request):
        md5 = request.GET.get('md5')
        img_name = md5 + '.jpg'
        path = os.path.join(settings.IMAGES_DIR, img_name)
        if os.path.exists(path):
            os.remove(path)
            message = 'remove success.'
        else:
            message = 'file(%s) not found.' % img_name
        # response = utils.response.wrap_json_response(message=message)
        response = self.wrap_json_response(code=utils.response.ReturnCode.SUCCESS, message=message)
        return JsonResponse(data=response,safe=False)

def image_text(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            return utils.response.wrap_json_response(code=utils.response.ReturnCode.RESOURCES_NOT_EXISTS)
        else:
            response_data = {}
            response_data['name'] = md5 + '.png'
            response_data['url'] = '/service/image?md5=%s' % (md5)
            response = utils.response.wrap_json_response(data=response_data)
            return JsonResponse(data=response, safe=False)


class ImageListView(View, utils.response.CommonResponseMixin):
    def get(self, request):
        image_files = os.listdir(settings.IMAGES_DIR)
        response_data = []
        for image_file in image_files:
            response_data.append({
                'name': image_file,
                'md5': image_file[:-4],
            })
        response = self.wrap_json_response(data=response_data)
        return JsonResponse(data=response)