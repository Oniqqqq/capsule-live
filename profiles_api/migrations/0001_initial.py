# Generated by Django 3.0.6 on 2020-09-11 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import profiles_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Capsule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capsule_name', models.CharField(max_length=255)),
                ('capsule_text', models.TextField(blank=True, max_length=360)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_to_open', models.DateTimeField()),
                ('isPaid', models.BooleanField(default=False)),
                ('notificationsent', models.BooleanField(default=False, null=True)),
                ('image_editor', models.ManyToManyField(blank=True, related_name='image_editor_user', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(default=1, on_delete=models.SET(profiles_api.models.get_deleted_user), related_name='owner_user', to=settings.AUTH_USER_MODEL)),
                ('shared_to', models.ManyToManyField(blank=True, related_name='shared_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CapsuleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capsule_file', models.FileField(blank=True, null=True, upload_to='media/covers/%Y/%m/%D/')),
                ('gallery_capsule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='profiles_api.Capsule')),
            ],
        ),
    ]
