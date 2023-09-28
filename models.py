from jsonfield import JSONField
from django.db import models
from chunked_upload.models import ChunkedUpload
from django.conf import settings
import uuid
from django.db.models import CharField, Value,F
from django.db.models.functions import Concat


# Create your models here.
MyChunkedUpload = ChunkedUpload


class Accesscontrol(models.Model):
    #id = models.AutoField(primary_key=True)
    CONCEPT_NM = models.CharField(db_column='CNCPT_NM', max_length=60)
    CNCPT_SHRT_NM = models.CharField(
        db_column='CNCPT_SHRT_NM', max_length=60)
    TRRTRY_NM = models.CharField(db_column='TRRTRY_NM', max_length=300)
    USER_ID= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=False,
    )
    BRAND_NM = JSONField(db_column='BRAND_NM', null=True)
    CATEGORY = models.CharField(db_column='CATEGORY', max_length=60, default='itm_brnd', null=True)
    ACTIVE = models.CharField(db_column='ACTIVE', max_length=60, default='1', null=True)

    def __str__(self):
        return str(self.USER_ID)

    class Meta:
        managed = True
        db_table = 'access_control'

# class BrandAccesscontrol(models.Model):
#     #id = models.AutoField(primary_key=True)
#     BRAND_NM = models.CharField(db_column='BRAND_NM', max_length=60)
#     USER_ID= models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         unique=True,
#     )

#     def __str__(self):
#         return str(self.USER_ID)

#     class Meta:
#         managed = True
#         db_table = 'access_control'


class Event_Metad(models.Model):
    #id = models.AutoField(primary_key=True)
    EVNT_ID = models.CharField(db_column='EVNT_ID', max_length=30, unique=True)
    EVNT_STRT_DT = models.CharField(db_column='EVNT_STRT_DT', max_length=300)
    EVNT_END_DT = models.CharField(db_column='EVNT_END_DT', max_length=300)
    EVNT_NM = models.CharField(db_column='EVNT_NM', max_length=300)
    EVNT_TYP = models.CharField(db_column='EVNT_TYP', max_length=300)
    EVNT_CRTE_DT = models.CharField(db_column='EVNT_CRTE_DT', max_length=300)
    USER_ID= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=False,
    )
    CNCPT_NM = models.CharField(db_column='CNCPT_NM', max_length=300)
    TRRTRY_NM = models.CharField(db_column='TRRTRY_NM', max_length=300)
    WKS_LFT = models.IntegerField(db_column='WKS_LFT')
    SALES_WKS = models.IntegerField(db_column='SALES_WKS')
    SPARE_WKS = models.IntegerField(db_column='SPARE_WKS')
    SSN_NM = models.CharField(db_column='SSN_NM', max_length=300)

    class Meta:
        managed = True
        db_table = 'event_metad'

    def __str__(self):
        return str(self.EVNT_ID)

class Version_metad(models.Model):
    #id = models.AutoField(primary_key=True)
    CNCPT_NM = models.CharField(db_column='CNCPT_NM',max_length=300)
    TRRTRY_NM = models.CharField(db_column='TRRTRY_NM', max_length=300)
    VRSN_ID = models.CharField(db_column='VRSN_ID', max_length=300, unique=True,)
    VRSN_NM = models.CharField(db_column='VRSN_NM', max_length=300,)
    EVNT_ID = models.ForeignKey(Event_Metad, to_field='EVNT_ID',
                                     db_column='EVNT_ID', max_length=300, on_delete=models.CASCADE, null=True)
    EVNT_NM = models.CharField(db_column='EVNT_NM', max_length=300,)
    VRSN_CRTE_DT = models.CharField(db_column='VRSN_CRTE_DT', max_length=300,)
    USER_ID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=False,
    )
    GRP_DPT = models.TextField(db_column='GRP_DPT',blank=True)
    BGTST = models.CharField(db_column='BGTST', max_length=300, null=True)
    BGTSTVAL = models.FloatField(db_column='BGTSTVAL', blank=True, null=True)
    MRKDWN_ELG = JSONField(db_column='MRKDWN_ELG', null=True)
    STK_PRFGRID = JSONField(db_column='STK_PRFGRID', null=True)
    SPR_WKS = models.CharField(db_column='SPR_WKS', max_length=300,)
    EVNT_TIMLIN = models.CharField(db_column='EVNT_TIMLIN', max_length=300,)
    BASE_SCENARIO_EXISTS = models.BooleanField(db_column='BASE_SCENARIO_EXISTS', default=False)
    LABEL = models.CharField(db_column='LABEL', default=False, max_length=300)

    class Meta:
        managed = True
        db_table = 'version_metad'
        #unique_together = (('EVNT_ID', 'VRSN_ID'),)
        constraints = [models.UniqueConstraint(
            fields=['EVNT_ID', 'VRSN_ID'], name='unique_IDs')]
    
    def __str__(self):
        return str(self.VRSN_ID)
