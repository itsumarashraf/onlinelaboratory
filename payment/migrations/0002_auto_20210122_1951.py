# Generated by Django 3.1.4 on 2021-01-22 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210121_2120'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetail',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.appointment'),
        ),
    ]