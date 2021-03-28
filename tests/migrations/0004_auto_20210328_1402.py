# Generated by Django 3.1.7 on 2021-03-28 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_writetask_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='LongWriteAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskNumber', models.IntegerField()),
                ('answer', models.TextField()),
                ('answerSheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.answersheet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
