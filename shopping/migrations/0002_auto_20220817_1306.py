# Generated by Django 3.1.5 on 2022-08-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loaddata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='loaddata',
            name='number_of_car',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='رقم العربية'),
        ),
    ]
