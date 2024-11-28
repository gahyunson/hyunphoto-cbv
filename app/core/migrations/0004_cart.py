# Generated by Django 3.2.25 on 2024-11-26 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_prices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.photos')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.prices')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]