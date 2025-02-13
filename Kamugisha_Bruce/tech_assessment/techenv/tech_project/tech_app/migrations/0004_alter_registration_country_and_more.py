# Generated by Django 4.2 on 2023-04-28 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_app', '0003_rename_registration_model_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='date_of_birth',
            field=models.DateField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='firstname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='lastname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='state_district',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='town',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='zipcode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
