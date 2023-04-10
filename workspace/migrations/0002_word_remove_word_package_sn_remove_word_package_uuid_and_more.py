# Generated by Django 4.1.7 on 2023-03-28 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('uuid', models.CharField(max_length=50)),
                ('sn', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='word_package',
            name='sn',
        ),
        migrations.RemoveField(
            model_name='word_package',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='word_package',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='workspace.word'),
        ),
    ]
