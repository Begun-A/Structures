from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=1042)
    price = models.FloatField()

    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Unit List'


class Structure(models.Model):
    name = models.CharField(max_length=1024)
    width = models.IntegerField()
    length = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE,
                             related_name='Structures')

    @property
    def area(self):
        return self.width * self.length

    @property
    def price(self):
        return self.area*self.unit.price

    class Meta:
        verbose_name = 'Structure'
        verbose_name_plural = 'Structure List'


class Room(models.Model):
    width = models.IntegerField()
    length = models.IntegerField()
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE,
                                  related_name='rooms')

    @property
    def area(self):
        return self.width * self.length

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Room List'
