import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from products.models import Product

def api_home(request, *args, **kwargs):
    # requests -> HttpRequest -> Django
    # request.body

    # print(request.GET) # get url query params
    # print(request.POST) # get url query params

    # body = request.body # byte string of JSON data
    # data = {}
    # try:
    #     data = json.loads(body) # string of Json data -> python dict
    # except: 
    #     pass

    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content-type'] = request.content_type
    
    # json.dumps(dict(request.headers))
    # return JsonResponse(data)

    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        # model instance (model_data)
        # turn a Python dict
        # serialization
        # return JSON to my client
        data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price'])

        return JsonResponse(data)
    # if using HttpResponse then
    # json_data_str = json.dumps(data)

    
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"}) 
    
    # return HttpResponse(data) # this will print a string
