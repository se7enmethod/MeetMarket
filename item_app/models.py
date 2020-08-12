from django.db import models
from craiglist_app.models import User, Review, UserManager
import re


class ItemManager(models.Manager):
    def item_validator(self, postData):
        errors = {}
        PRICE_REGEX = re.compile(r'^[0-9.]+$')
        if not PRICE_REGEX.match(postData['price']):
            errors['price'] = "Please enter a valid price!"
        CONDITION_REGEX = re.compile(r'^[a-zA-Z]+$')
        if not CONDITION_REGEX.match(postData['condition']):
            errors['condition'] = "Only letters can be used in the condition field!"
        if len(postData['name']) < 2:
            errors['name'] = "Name must be at least 2 characters long!"
        if len(postData['description']) < 2:
            errors['description'] = "Description is required!"
        # if len(postData['password']) < 8:
        #     errors['password'] = "Password must be at least 8 characters long!"
        if len(postData['condition']) < 2:
            errors['condition'] = "Condition must be at least 2 characters long!"
        return errors
# Options for P2 if we make it validations for limiting to 5listings a day per user


class Category(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Item(models.Model):
    user = models.ForeignKey(User, related_name="items",
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    condition = models.CharField(max_length=25)
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE)
    # image = models.ImageField()
    # from documentation
    # import form -> forms.FileField()
    flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()


class Image(models.Model):
    item = models.ForeignKey(
        Item, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    user = models.ForeignKey(
        User, related_name="messages", on_delete=models.CASCADE)
    item = models.ForeignKey(
        Item, related_name="messages", on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    message = models.ForeignKey(
        Message, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
