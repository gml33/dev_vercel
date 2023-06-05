# Generated by Django 4.2.1 on 2023-06-04 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0009_alter_derivacion_paciente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evolucion',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.paciente'),
        ),
        migrations.AlterField(
            model_name='evolucion',
            name='profesional_responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
