from django.contrib.gis.db import models
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class Excavation_unit(models.Model):
    unit = models.CharField(max_length=6,blank=False)
    extent = models.GeometryField(dim=3,blank=True,null=True,srid=-1)
    objects = models.GeoManager()
    class Meta:
        managed = True
        db_table = 'units'
        verbose_name_plural = "Excavation units"
        verbose_name = "Excavation Unit"
    def __unicode__(self):
        return u'%s' % (self.unit)


class Context(models.Model):
    cat_no = models.CharField(max_length=12,blank=False)
    collection = models.CharField(max_length=15,blank=False)
    unit = models.CharField(max_length=6,blank=False)
    id_no = models.CharField('ID',max_length=6,blank=False)
    sector = models.CharField(max_length=50,blank=True,null=True)
    analytical_level = models.CharField(max_length=50,blank=True,null=True)
    level = models.CharField(max_length=50,blank=True,null=True)
    code = models.CharField(max_length=25,blank=True,null=True)
    exc_date = models.DateField('Date',blank=True,null=True)
    excavator =models.CharField(max_length=50,blank=True,null=True)
    points = models.GeometryField(dim=3,blank=True, null=True,srid=-1)
    objects = models.GeoManager()
    class Meta:
        managed = True
        db_table = 'context'
        verbose_name_plural = "Context (Catalog)"
        verbose_name = "Context"
    def __unicode__(self):
        return u'%s' % (self.cat_no)


class Refits(models.Model):
    unit = models.CharField(max_length=6,blank=False)
    id_no = models.CharField('ID',max_length=6,blank=False)
    counter = models.IntegerField(blank=True,null=True)
    class Meta:
        managed = True
        db_table = 'refits'
        verbose_name_plural = "Refits"
        verbose_name = "Refit"


class Lithic(Context):
    dataclass = models.CharField(max_length=20,blank=False)
    raw_material = models.CharField(max_length=20,blank=True,null=True)
    support = models.CharField(max_length=20,blank=True,null=True)
    technique = models.CharField(max_length=20,blank=True,null=True)
    form = models.CharField(max_length=20,blank=True,null=True)
    fb_type = models.IntegerField('Bordes Type',blank=True,null=True)
    fb_type_2 = models.IntegerField('Bordes Type 2',blank=True,null=True)
    core_type = models.CharField(max_length=20,blank=True,null=True)
    biface_type = models.CharField(max_length=20,blank=True,null=True)
    retouched_edges = models.IntegerField(blank=True,null=True)
    retouch_intensity = models.CharField(max_length=20,blank=True,null=True)
    tf_character = models.CharField(max_length=20,blank=True,null=True)
    tf_surface = models.CharField(max_length=20,blank=True,null=True)
    tf_location = models.CharField(max_length=20,blank=True,null=True)
    platform_surface = models.CharField(max_length=20,blank=True,null=True)
    platform_exterior = models.CharField(max_length=20,blank=True,null=True)
    core_faces = models.IntegerField(blank=True,null=True)
    platforms = models.CharField(max_length=20,blank=True,null=True)
    platform_technique_1 = models.CharField(max_length=20,blank=True,null=True)
    platform_technique_2 = models.CharField(max_length=20,blank=True,null=True)
    scar_morphology = models.CharField(max_length=20,blank=True,null=True)
    cortex = models.CharField(max_length=12,blank=True,null=True)
    discard = models.CharField(max_length=20,blank=True,null=True)
    edge_damage = models.CharField(max_length=20,blank=True,null=True)
    alteration = models.CharField(max_length=20,blank=True,null=True)
    proximal_removals = models.IntegerField(blank=True,null=True)
    scar_length = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    length = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    width = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    thickness = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    platform_width = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    platform_thickness = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    small_pw = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    bulb = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    epa = models.IntegerField(blank=True,null=True)
    weight = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    class Meta:
        managed = True
        db_table = 'lithics'


class Fauna(Context):
    tentative_ID = models.CharField(max_length=20,blank=True,null=True)
    genus = models.CharField(max_length=30,blank=True,null=True)
    side = models.CharField(max_length=5,blank=True,null=True)
    part = models.CharField(max_length=30,blank=True,null=True)
    portion = models.CharField(max_length=30,blank=True,null=True)
    segment = models.CharField(max_length=30,blank=True,null=True)
    bone_type = models.CharField(max_length=30,blank=True,null=True)
    class Meta:
        managed = True
        db_table = 'fauna'
        verbose_name_plural = "Fauna"
        verbose_name = "Fauna"


class Small_Find(Context):
    screen_size = models.CharField(max_length=20,blank=True,null=True)
    platform_count = models.IntegerField(blank=True,null=True)
    platform_weight = models.IntegerField(blank=True,null=True)
    class Meta:
        managed = True
        db_table = 'small_finds'
        verbose_name_plural = "Small Finds (Summary Counts by bucket)"
        verbose_name = "Small find (bucket)"


class Small_Find_Weights(models.Model):
    smalls_id = models.AutoField('ID',primary_key=True)
    context = models.ForeignKey(Context)
    weight = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    class Meta:
        managed = True
        db_table = 'small_find_weights'
        verbose_name_plural = "Small Finds (Weights by piece)"
        verbose_name = "an artifact in a bucket"


class Granulometry(models.Model):
    grain_id = models.AutoField('ID',primary_key=True)
    context = models.ForeignKey(Context)
    weight = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    class Meta:
        managed = True
        db_table = 'granulometry'
        verbose_name_plural = "Granulometry"
        verbose_name = "a stone in a granulometry bucket"


class Galet_Weights(Context):
    weight = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    class Meta:
        managed = True
        db_table = 'galet_weights'
        verbose_name_plural = "Galet Weights"
        verbose_name = "Galet Weight"


class Photo(Context):
    image01 = models.ImageField('Image',upload_to='/media/',null=True,blank=True)
    def thumb01(self):
        return u'<a href="%s"><img src="%s" style="width:300px" /></a>' % (os.path.join('/static/' + self.image01.url),os.path.join('/static/' + self.image01.url))
    thumb01.short_description = 'Image'
    thumb01.allow_tags = True
    thumb01.mark_safe = True
    def thumb02(self):
        return u'<a href="%s"><img src="%s" style="width:100px" /></a>' % (os.path.join('/static/' + self.image01.url),os.path.join('/static/' + self.image01.url))
    thumb02.short_description = 'Image'
    thumb02.allow_tags = True
    thumb02.mark_safe = True
    class Meta:
        managed = True
        db_table = 'photos'


class Lithics_with_Photos(Context):
    class Meta:
        proxy = True
        managed = True
        verbose_name_plural = "Lithics (only with photos)"
        verbose_name = "Lithic (only with photo)"


class Buckets_with_Grains(Context):
    class Meta:
        proxy = True
        managed = True
        verbose_name_plural = "Buckets with Granulometry"
        verbose_name = "Bucket with Granulometry"


class Small_find_weights_summary(Context):
    class Meta:
        proxy = True
        managed = True
        verbose_name_plural = "Small Finds (Weights by bucket)"
        verbose_name = "Weights of small finds in a bucket"
