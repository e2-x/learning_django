# Generated by Django 2.2.4 on 2019-08-08 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrecord',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_app.Webpage'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_app.Topic'),
        ),
    ]
