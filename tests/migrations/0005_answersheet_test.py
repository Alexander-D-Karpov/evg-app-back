# Generated by Django 3.1.7 on 2021-03-28 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_auto_20210328_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='answersheet',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.test'),
        ),
    ]
