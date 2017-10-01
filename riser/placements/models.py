from django.db import models


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    username = models.CharField(max_length=120)


class Company(models.Model):
    registration = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=200)


class Placement(models.Model):
    DECLINED = 'Declined'
    APPROVED = 'Approved'
    PENDING = 'Pending'
    NOT_SUBMITTED = 'NOT_Submitted'

    reference = models.AutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20,
                              choices=(
                                  (APPROVED, 'Approved'),
                                  (PENDING, 'Pending'),
                                  (NOT_SUBMITTED, 'Not Submitted'),
                                  (DECLINED, 'Declined'),
                              ),
                              default=NOT_SUBMITTED)
    candidate = models.ForeignKey(Candidate)
    company = models.ForeignKey(Company)
