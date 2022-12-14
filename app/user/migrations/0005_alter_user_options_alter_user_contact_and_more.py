# Generated by Django 4.1.3 on 2022-11-15 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_first_name_remove_user_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '使用者', 'verbose_name_plural': '使用者'},
        ),
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(blank=True, help_text='分機', max_length=100, null=True, verbose_name='聯絡方式'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='unit',
            field=models.CharField(blank=True, help_text='單位', max_length=100, null=True, verbose_name='單位'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='姓名', max_length=255, verbose_name='姓名'),
        ),
    ]
