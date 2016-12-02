from django.db import models


class UnitORM(models.Model):
    name = models.CharField()
    price = models.FloatField()


class StructureORM(models.Model):
    name = models.CharField()
    width = models.IntegerField()
    length = models.IntegerField()
    unit = models.ForeignKey(UnitORM, on_delete=models.CASCADE,
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


class RoomORM(models.Model):
    width = models.IntegerField()
    length = models.IntegerField()
    structure = models.ForeignKey(StructureORM, on_delete=models.CASCADE,
                                  related_name='rooms')

    @property
    def area(self):
        return self.width * self.length

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Room List'
