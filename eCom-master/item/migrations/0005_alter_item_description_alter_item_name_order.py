# Generated by Django 4.1.3 on 2024-03-28 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import item.validations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0004_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(validators=[item.validations.validate_description]),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, validators=[item.validations.validate_name]),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[item.validations.validate_name])),
                ('card_info', models.CharField(max_length=16, validators=[item.validations.validate_card])),
                ('address', models.TextField(validators=[item.validations.validate_description])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='item.item')),
            ],
            options={
                'verbose_name_plural': 'orders',
                'ordering': ('-created_at',),
            },
        ),
    ]
