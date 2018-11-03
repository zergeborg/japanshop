# Generated by Django 2.1 on 2018-11-03 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0002_auto_20181103_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hungarian_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_hu_adr', to='product.HungarianAddress', verbose_name='hungarian_address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='hungarian_billing_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_hu_bill_adr', to='product.HungarianAddress', verbose_name='hungarian_billing_address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='japanese_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_jp_adr', to='product.JapaneseAddress', verbose_name='japanese_address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='japanese_billing_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_jp_bill_adr', to='product.JapaneseAddress', verbose_name='japanese_billing_address'),
        ),
    ]