# Generated by Django 3.0.3 on 2020-07-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    operations = [
        migrations.CreateModel(
            name='AllProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(default='description')),
                ('disprice', models.IntegerField(default=0)),
                ('batch', models.DateTimeField(default='2019-12-25 12:30')),
                ('sale', models.BooleanField(default=False)),
            ],
        ),
    ]