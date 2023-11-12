# Generated by Django 4.2.6 on 2023-11-12 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='changing_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last changed date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateTimeField(verbose_name='Creation date'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_version', models.IntegerField(verbose_name='Version number')),
                ('title_version', models.CharField(max_length=50, verbose_name='Version name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Current version indicator')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Version',
                'verbose_name_plural': 'Versions',
            },
        ),
    ]