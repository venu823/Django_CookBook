# Generated by Django 2.2 on 2020-02-27 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0002_heroacquaintance'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroacquaintance',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entities.Category'),
        ),
        migrations.AlterField(
            model_name='heroacquaintance',
            name='hero',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entities.Hero'),
        ),
    ]
