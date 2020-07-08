from http import HTTPStatus
from urllib.parse import urlparse
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from scrapyd_api import ScrapydAPI
from main.models import HoroscopeItem
from datetime import date


scrapyd = ScrapydAPI('http://localhost:6800')


def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)
    except ValidationError:
        return False

    return True


class SchedulingError(Exception):
    def __str__(self):
        return 'scheduling error'

@csrf_exempt
@require_http_methods(['POST', 'GET'])
def crawl(request):
    if request.method == 'POST':
        url = request.POST.get('url', None)
        if not url:
            return JsonResponse(
                {'error': 'No URL'},
                 status=HTTPStatus.BAD_REQUEST
            )
        if not is_valid_url(url):
            return JsonResponse(
                {'error': 'URL is not valid'},
                status=HTTPStatus.BAD_REQUEST
            )
        forecastDay = request.POST.get('forecastDay', "today")
        domain = urlparse(url).netloc
        unique_id = str(uuid4())

        settings = {
            'unique_id': unique_id,
            'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        }
        try:
            HoroscopeItem.objects.all().delete()
            task = scrapyd.schedule('default', 'hcrawler', settings=settings, url=url, day =forecastDay,domain=domain)
        except SchedulingError as e:
            return JsonResponse(
                {'error': e},
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
        return JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started'})
    elif request.method == 'GET':
        try:
            task_id = request.GET.get('task_id', None)
        except ValueError as e:
            return JsonResponse(
                {'error': e},
                status=HTTPStatus.BAD_REQUEST
            )
        try:
            unique_id = request.GET.get('unique_id', None)[:-1]
        except ValueError as e:
            return JsonResponse(
                {'error': e},
                status=HTTPStatus.BAD_REQUEST
            )
        status = scrapyd.job_status('default', task_id)
        if status == 'finished':
            try:
                item = HoroscopeItem.objects.filter(unique_id=unique_id)
                if not item:
                    return JsonResponse(
                        {'error': 'There is no data'},
                        status=HTTPStatus.NOT_FOUND
                    )
                dict_list = []
                for i in list(item):
                    dict_data = {
                        'sign_name': i.sign_name,
                        'date_range': i.date_range,
                        'current_date': i.current_date.strftime('%Y-%m-%d'),
                        'description': i.description,
                        'compatibility': i.compatibility,
                        'mood': i.mood,
                        'color': i.color,
                        'lucky_number':i.lucky_number,
                        'lucky_time':i.lucky_time
                    }
                    dict_list.append(dict_data)
                data = {'data': dict_list}
                return JsonResponse(data)
            except Exception as e:
                return JsonResponse(
                    {'error': str(e)},
                )
        else:
            return JsonResponse({'status': status})


def show_data(request):
    sunshine = request.GET.get('sunshine', None)
    item = HoroscopeItem.objects.filter(sign_name=sunshine)
    if not item:
        return JsonResponse(
            {'error': 'There is no data in database'},
            status=HTTPStatus.NOT_FOUND
        )
    dict_list = []
    for i in list(item):
        dict_data = {
            'sign_name': i.sign_name,
            'date_range': i.date_range,
            'current_date': i.current_date.strftime('%Y-%m-%d'),
            'description': i.description,
            'compatibility': i.compatibility,
            'mood': i.mood,
            'color': i.color,
            'lucky_number':i.lucky_number,
            'lucky_time':i.lucky_time
        }
        dict_list.append(dict_data)
    data = {'data': dict_list}
    return JsonResponse(data)

