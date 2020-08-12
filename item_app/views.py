from django.shortcuts import render, redirect
from craiglist_app.models import User, Review
from item_app.models import Category, Item, Image, Message, Comment, ItemManager
from django.contrib import messages
from time import strftime, gmtime
from django.core.files.storage import FileSystemStorage

# SESSION INFO:
# request.session['log_email'] = []
# request.session['log_password'] = []
# request.session['log_first_name'] = []
# request.session['log_last_name'] = []
# request.session['log_location'] = []


def index(request):
    return render(request, "index.html")


def new_item(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "this_user": User.objects.get(email=request.session['log_email'])
    }
    return render(request, "new.html", context)


def create_item(request):
    errors = Item.objects.item_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('item:my_new_item')
    else:
        if request.method == "POST":
            logged_user = User.objects.filter(
                email=request.session['log_email'])
            name = request.POST['name']
            price = request.POST['price']
            description = request.POST['description']
            condition = request.POST['condition']
            category_name = request.POST['category']
            location = request.POST['location']
            image = request.FILES['images']
            fs = FileSystemStorage()
            image_name = fs.save(image.name, image)
            url = fs.url(image_name)
            category = Category.objects.get(name=category_name)
            new_item = Item.objects.create(user=logged_user[0],
                                           name=name, price=price, description=description, condition=condition, category=category, location=location)
            item_id = new_item.id
            new_image = Image.objects.create(item=new_item, image=image)
            print(item_id)
        return redirect('item:my_item_info', item_id)


def edit(request, item_id):
    # grab this_item info to push to edit template
    this_item = Item.objects.get(id=item_id)
    images = this_item.images.all()
    if len(images) > 0:
        image = images[0]
        context = {
            "this_item": this_item,
            "all_categories": Category.objects.all(),
            "this_user": User.objects.get(email=request.session['log_email']),
            "images": images,
            "image": image,
        }
    else:
        context = {
            "this_item": this_item,
            "all_categories": Category.objects.all(),
            "this_user": User.objects.get(email=request.session['log_email']),
            "images": images,
        }
    return render(request, "edit.html", context)


def post_edit(request, item_id):
    errors = Item.objects.item_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('item:my_edit_item', item_id)
    else:
        if request.method == "POST":
            this_item = Item.objects.get(id=item_id)
            logged_user = User.objects.filter(
                email=request.session['log_email'])
            this_item.name = request.POST['name']
            this_item.price = request.POST['price']
            this_item.description = request.POST['description']
            this_item.location = request.POST['location']
            this_item.condition = request.POST['condition']
            this_item.category.name = request.POST['category']
            pics = this_item.images.all()
            if len(pics) == 0:
                image = request.FILES['images']
                fs = FileSystemStorage()
                image_name = fs.save(image.name, image)
                url = fs.url(image_name)
                new_image = Image.objects.create(item=this_item, image=image)
            this_item.save()
    return redirect('item:my_item_info', item_id)


def delete(request, item_id):
    this_item = Item.objects.get(id=item_id)
    this_item.delete()
    return redirect('login:my_admin_controls')


def item_info(request, item_id):
    item = Item.objects.get(id=item_id)
    messages = item.messages.all()
    images = item.images.all()
    this_user = User.objects.get(email=request.session['log_email'])
    print("this is the user", this_user)
    context = {
        "item": item,
        "messages": messages,
        "time": strftime("%m-%d-%y"),
        "images": images,
        "this_user": this_user,
    }
    return render(request, "item_info.html", context)


def category_page(request, category_id):
    category = Category.objects.get(id=category_id)
    items_in_cat = category.items.all()
    context = {
        "category": category,
        "items_in_cat": items_in_cat,
    }
    return render(request, "category.html", context)


def user_page(request, user_id):
    user = User.objects.get(id=user_id)
    logged_user = User.objects.get(email=request.session['log_email'])
    items = user.items.all()
    reviews = user.reviews.all()
    new = 0
    if len(reviews) > 0:
        total = 0
        for review in reviews:
            total += int(review.rating)
        avg = total / len(reviews)
        new = "%.2f" % avg
    context = {
        "user": user,
        "items": items,
        "reviews": reviews,
        "avg": new,
        "logged_user": logged_user,
    }
    return render(request, "userpage.html", context)


def new_review(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        user = User.objects.get(id=user_id)
        review = request.POST['review']
        rating = int(request.POST['rating'])
        new_review = Review.objects.create(
            user=user, content=review, rating=rating)
    return redirect('item:my_user_page', user_id)


def post_message(request):
    if request.method == "POST":
        logged_user = User.objects.filter(
            email=request.session['log_email'])
        message = request.POST['message']
        item_id = request.POST['item_id']
        item = Item.objects.get(id=item_id)
        new_message = Message.objects.create(
            user=logged_user[0], item=item, message=message)
    return redirect('item:my_item_info', item_id)


def post_comment(request):
    if request.method == "POST":
        logged_user = User.objects.filter(
            email=request.session['log_email'])
        message_id = request.POST['messageid']
        message = Message.objects.get(id=message_id)
        comment = request.POST['comment']
        item_id = request.POST['itemid']
        new_comment = Comment.objects.create(
            message=message, user=logged_user[0], comment=comment)
    return redirect('item:my_item_info', item_id)


def all_listings(request):
    logged_user = User.objects.filter(email=request.session['log_email'])
    user_admin = logged_user[0].admin
    all_items = Item.objects.all()
    context = {
        "user_admin": user_admin,
        "items": all_items,
    }

    return render(request, "allitems.html", context)


def all_categories(request):
    logged_user = User.objects.filter(email=request.session['log_email'])
    user_admin = logged_user[0].admin
    all_categories = Category.objects.all()
    context = {
        "user_admin": user_admin,
        "categories": all_categories,
    }

    return render(request, "allcategories.html", context)


def flag_item(request, item_id):
    flag_this_item = Item.objects.get(id=item_id)
    flag_this_item.flag = True
    flag_this_item.save()
    print(
        f"this item has been flagged: {flag_this_item} - {flag_this_item.flag}")
    return redirect('item:my_item_info', item_id)


def admin_flag_control(request, item_id):
    if request.method == "POST":
        flag_this_item = Item.objects.get(id=item_id)
        flag_this_item.flag = request.POST['flag']
        flag_this_item.save()
    return redirect('item:my_item_info', item_id)
