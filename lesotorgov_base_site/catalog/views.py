from django.shortcuts import render
from .models import Type, Variety, Lumber, LumberInstance, StampCement, Cement, CementInstance, StampMetal, Metal, \
    MetalInstance
from django.views import generic


# Create your views here.
def lumber_list(request):
    data = Lumber.objects.all()
    return render(request, 'lumber_list.html', {'data': data})


def lumber_detail(request):
    data = Lumber.objects.all()
    return render(request, 'lumber_detail.html', {'data': data})


def cement_list(request):
    data = Cement.objects.all()
    return render(request, 'cement_list.html', {'data': data})


def metal_list(request):
    data = Metal.objects.all()
    return render(request, 'metal_list.html', {'data': data})


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_lumbers = Lumber.objects.all().count()
    num_instances = LumberInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = LumberInstance.objects.filter(status__exact='a').count()
    num_types = Type.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_lumbers': num_lumbers,
                 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_types': num_types},
    )


class LumberListView(generic.ListView):
    model = Lumber
    paginate_by = 6


class LumberDetailView(generic.DetailView):
    model = Lumber


class TypeListView(generic.ListView):
    model = Type


class TypeDetailView(generic.DetailView):
    model = Type


class CementListView(generic.ListView):
    model = Cement


class CementDetailView(generic.DetailView):
    model = Cement


class StampCementListView(generic.ListView):
    model = StampCement


class StampCementDetailView(generic.DetailView):
    model = StampCement


class MetalListView(generic.ListView):
    model = Metal


class MetalDetailView(generic.DetailView):
    model = Metal


class StampMetalListView(generic.ListView):
    model = StampMetal


class StampMetalDetailView(generic.DetailView):
    model = StampMetal
# TODO номер госта и ссылка на гост,отдельная таблица для тех. характеристик, фотография и описание
