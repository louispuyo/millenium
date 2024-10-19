# Generated by Django 4.2.5 on 2024-10-14 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_user_wallet_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='wallet_id',
        ),
        migrations.AddField(
            model_name='user',
            name='wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.wallet'),
        ),
    ]
