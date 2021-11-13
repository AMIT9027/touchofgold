# Generated by Django 3.2.9 on 2021-11-10 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activity_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ad_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('thumb_firstpage', models.ImageField(upload_to='static/Banner_img')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('company_name', models.CharField(max_length=200)),
                ('gst_no', models.CharField(max_length=120)),
                ('area_pin_code', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=140)),
                ('phone', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.magazine')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='sub_mag_activity_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smac_count', models.CharField(max_length=200)),
                ('smac_activity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.activity_type')),
                ('smac_magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.magazine')),
                ('smac_subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='sub_mag_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sma_time', models.DateTimeField(auto_now_add=True)),
                ('sma_activity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.activity_type')),
                ('sma_magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.magazine')),
                ('sma_subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='mag_edition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb_firstpage', models.ImageField(upload_to='static/Banner_img')),
                ('thumb_secondthird', models.ImageField(upload_to='static/Banner_img')),
                ('summary_title', models.ImageField(upload_to='static/Banner_img')),
                ('summary_para', models.TextField()),
                ('pdf_path', models.CharField(max_length=200)),
                ('latest_section_title', models.CharField(max_length=150)),
                ('previous_section_title', models.CharField(max_length=150)),
                ('edition', models.CharField(max_length=300)),
                ('edition_description', models.CharField(max_length=300)),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.magazine')),
            ],
        ),
        migrations.CreateModel(
            name='mag_edit_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/Banner_img')),
                ('mag_edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.mag_edition')),
            ],
        ),
        migrations.CreateModel(
            name='mag_book_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Images', models.ImageField(default=' ', upload_to='', verbose_name='Magazine_Pages')),
                ('mag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mag_images', to='gold.mag_edit_page')),
            ],
        ),
        migrations.CreateModel(
            name='mag_activity_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_count', models.CharField(max_length=200)),
                ('mac_activity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.activity_type')),
                ('mac_magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.magazine')),
            ],
        ),
        migrations.CreateModel(
            name='ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.CharField(max_length=200)),
                ('img_width', models.CharField(max_length=250)),
                ('img_height', models.CharField(max_length=250)),
                ('video_link', models.CharField(max_length=200)),
                ('promo_text', models.CharField(max_length=150)),
                ('call_to_action_text', models.CharField(max_length=250)),
                ('call_to_action_link', models.CharField(max_length=300)),
                ('ad_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.ad_section')),
            ],
        ),
    ]