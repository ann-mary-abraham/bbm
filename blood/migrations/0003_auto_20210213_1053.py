

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
        ('donor', '0001_initial'),
        ('blood', '0002_bloodrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloodrequest',
            old_name='age',
            new_name='patient_age',
        ),
        migrations.RenameField(
            model_name='bloodrequest',
            old_name='name',
            new_name='patient_name',
        ),
        migrations.RemoveField(
            model_name='bloodrequest',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='bloodrequest',
            name='mobile',
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='request_by_donor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donor.Donor'),
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='request_by_patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient'),
        ),
    ]
