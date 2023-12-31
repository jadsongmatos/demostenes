# Generated by Django 4.1 on 2023-11-07 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0002_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ordereds',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=1)),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ordereds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedsTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ordereds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ordereds')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('length', models.SmallIntegerField(blank=True, null=True)),
                ('price', models.SmallIntegerField(blank=True, null=True)),
                ('discount', models.SmallIntegerField(blank=True, null=True)),
                ('rate', models.SmallIntegerField(blank=True, null=True)),
                ('id_ordereds', models.UUIDField(blank=True, null=True)),
                ('id_products', models.UUIDField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('stock', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('id_category', models.UUIDField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('valor', models.SmallIntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('ordereds', models.ManyToManyField(through='web.OrderedsTransactions', to='web.ordereds')),
            ],
        ),
        migrations.AddField(
            model_name='orderedstransactions',
            name='id_transactions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.transaction'),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('nation', models.CharField(max_length=255)),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contact', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='orderedstransactions',
            unique_together={('id_ordereds', 'id_transactions')},
        ),
    ]
