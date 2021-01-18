from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
import enum


class User(AbstractUser):
    # django 3에서 가능한 문법
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13,
                                    validators=[RegexValidator(r"^010[1-9]\d{7}$")],
                                    blank=True,
                                    help_text="'-'를 제외한 숫자를 입력해주세요.")
    gender = models.CharField(max_length=1,
                              choices=GenderChoices.choices,
                              blank=True)
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%Y/%m/%d",
                               help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요.")
