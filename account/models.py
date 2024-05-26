from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, Phone, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not Phone:
            raise ValueError("Users must have an email address")

        user = self.model(
            Phone=self.normalize_email(Phone),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Phone, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            Phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="ادرس ایمیل",
        max_length=255,
        null= True,
        blank=True,
        unique=True,
    )
    Fullname = models.CharField(max_length=50,verbose_name="نام کامل")
    Phone = models.CharField(max_length=11, unique=True, verbose_name="شماره تلفن")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False,verbose_name="ادمین")

    objects = UserManager()

    USERNAME_FIELD = "Phone"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name='کاربر'
        verbose_name_plural='کاربرها'

    def __str__(self):
        return self.Phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class user_otp(models.Model):
    token = models.CharField(max_length=200,null=True)
    Phone = models.CharField(max_length=11)
    code = models.SmallIntegerField()
    expiration_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Phone



class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Addresses")
    full_name = models.CharField(max_length=60)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=500)
    postal_code = models.CharField(max_length=25)

    def __str__(self):
        return self.user.Phone

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name= models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/profile',blank=True, null=True)


    def __str__(self):
        return self.user.Phone
