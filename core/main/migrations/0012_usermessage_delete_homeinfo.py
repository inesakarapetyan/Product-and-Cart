# Generated by Django 5.0.6 on 2024-06-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_homeinfo_remove_pay_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('phone', models.CharField(max_length=60, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.TextField(verbose_name='Address')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
        migrations.DeleteModel(
            name='HomeInfo',
        ),
    ]
