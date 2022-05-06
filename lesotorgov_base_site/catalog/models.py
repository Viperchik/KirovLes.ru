from django.db import models
from django.urls import reverse


# Create your models here.


class Type(models.Model):
    """
    Модель показывает сорт доски
    """
    title = models.CharField(max_length=100, help_text='Введите сорт пиломатериала')
    summary = models.TextField(max_length=500, null=True, help_text='Введите описание сорта')

    def __str__(self):
        """
        Функция для возврата объекта модели(Для админа)

        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular variety instance.
        """
        return reverse('type-detail', args=[str(self.id)])


class Variety(models.Model):
    """
    Модель представляет вид пиломатериала
    """
    title = models.CharField(max_length=50, help_text='Введите название вида')

    def __str__(self):
        """

        """
        return '{0}'.format(self.title)


class Lumber(models.Model):
    """
    Модель представляет общий вид пиломатериала
    """
    title = models.CharField(max_length=50, help_text='Введите название пиломатериала(Для удобного поиска)')
    variety = models.ForeignKey(Variety, on_delete=models.SET_NULL, null=True, help_text='Выберите вид пиломатериала')
    size = models.TextField(max_length=15, help_text='Введите размер пиломатериала')
    num_in_cube = models.FloatField(max_length=20, help_text='Введите количетсво пиломатериала в 1 кубическом метре')
    gost = models.CharField(max_length=50, null=True, help_text='Введите ГОСТ металла')
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, help_text='Выберите сорт пиломатериала')
    img = models.ImageField(upload_to='img/', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Возвращает ссылку на вид пиломатериала
        """
        return reverse('lumber-detail', args=[str(self.id)])


class LumberInstance(models.Model):
    """
    Модель отображает конкретный вид доски
    """

    id = models.IntegerField(primary_key=True, default=None, help_text='Введите id для этого вида пиломатериала')
    lumber = models.ForeignKey(Lumber, on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    count = models.CharField(default=None, max_length=10, help_text='Количество пиломатериала')
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, help_text='Выберите сорт пиломатериала')
    LOAN_STATUS = (
        ('д', 'доступно'),
        ('з', 'зарезервированно'),
        ('о', 'отсутствует')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='о',
                              help_text='Доступность пиломатериала')

    class Meta:
        ordering = ['type']

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} {1}'.format(self.id, self.lumber.title)


class StampCement(models.Model):
    """
    Модель представляет марку цемента
    """
    title = models.CharField(max_length=50, help_text='Введите название марки')
    summary = models.TextField(max_length=500, null=True, help_text='Введите описание марки')

    def get_absolute_url(self):
        """
        Returns the url to access a particular variety instance.
        """
        return reverse('stamp_cement-detail', args=[str(self.id)])

    def __str__(self):
        """

        """
        return '{0}'.format(self.title)


class Cement(models.Model):
    """
    Модель представляет общий вид цемента
    """
    title = models.CharField(max_length=50, help_text='Введите название цемента(Для удобного поиска)')
    stamp = models.ForeignKey(StampCement, on_delete=models.SET_NULL, null=True, help_text='Выберите марку цемента')
    gost = models.CharField(max_length=50, null=True, help_text='Введите ГОСТ металла')
    img = models.ImageField(upload_to='img/', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Возвращает ссылку на вид цемента
        """
        return reverse('cement-detail', args=[str(self.id)])


class CementInstance(models.Model):
    """
    Модель отображает конкретный вид цемента
    """

    id = models.IntegerField(primary_key=True, default=None, help_text='Введите id для этого вида цемента')
    cement = models.ForeignKey(Cement, on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    count = models.CharField(default=None, max_length=10, help_text='Количество цемента')

    LOAN_STATUS = (
        ('д', 'доступно'),
        ('з', 'зарезервированно'),
        ('о', 'отсутствует')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='о',
                              help_text='Доступность цемента')

    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} {1}'.format(self.id, self.cement.title)


class StampMetal(models.Model):
    """
    Модель представляет марку металла
    """
    title = models.CharField(max_length=50, help_text='Введите название марки')
    summary = models.TextField(max_length=500, null=True, help_text='Введите описание марки')

    def get_absolute_url(self):
        """
        Returns the url to access a particular variety instance.
        """
        return reverse('stamp_metal-detail', args=[str(self.id)])

    def __str__(self):
        """

        """
        return '{0}'.format(self.title)


class Metal(models.Model):
    """
    Модель представляет общий вид металла
    """
    title = models.CharField(max_length=50, help_text='Введите название металла(Для удобного поиска)')
    stamp = models.ForeignKey(StampMetal, on_delete=models.SET_NULL, null=True, help_text='Выберите марку металла')
    size = models.TextField(max_length=15, help_text='Введите размер металла')
    gost = models.CharField(max_length=50, null=True, help_text='Введите ГОСТ металла')
    img = models.ImageField(upload_to='img/', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Возвращает ссылку на вид металла
        """
        return reverse('metal-detail', args=[str(self.id)])


class MetalInstance(models.Model):
    """
    Модель отображает конкретный вид цемента
    """

    id = models.IntegerField(primary_key=True, default=None, help_text='Введите id для этого вида металла')
    metal = models.ForeignKey(Metal, on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    count = models.CharField(default=None, max_length=10, help_text='Количество металла')

    LOAN_STATUS = (
        ('д', 'доступно'),
        ('з', 'зарезервированно'),
        ('о', 'отсутствует')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='о',
                              help_text='Доступность металла')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} {1}'.format(self.id, self.metal.title)
