# Generated by Django 3.2.3 on 2021-05-25 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0031_auto_20210525_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='Biblioteca',
        ),
        migrations.CreateModel(
            name='ItemBiblioteca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('Livro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='escola.livro')),
            ],
        ),
    ]