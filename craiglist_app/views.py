from django.shortcuts import render, redirect
from craiglist_app.models import User, Review
from item_app.models import Category, Item, Image, Message, Comment
from django.contrib import messages
import bcrypt


def index(request):
    request.session['log_email'] = []
    request.session['log_password'] = []
    request.session['log_first_name'] = []
    request.session['log_last_name'] = []
    request.session['log_location'] = []
    return render(request, "index.html")


def register_page(request):
    return render(request, "register.html")


def log_in(request):
    errors = User.objects.log_in_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('login:my_index')
    else:
        if request.method == "POST":
            log_email = request.POST['log_email']
            log_pw = request.POST['log_pw']
            if User.objects.filter(email=log_email):
                request.session['log_email'] = log_email
                request.session['log_pw'] = log_pw
                return redirect('login:my_successful_log_in')


def register(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('login:my_register_page')
    else:
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            location = request.POST['location']
            pw = request.POST['password']
            confirm_pw = request.POST['confirm_pw']
            pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
            # confirm password stuff here
            if bcrypt.checkpw(confirm_pw.encode(), pw_hash.encode()) == True:
                User.objects.create(first_name=first_name, last_name=last_name,
                                    email=email, location=location, password=pw_hash)
                request.session['log_email'] = email
                request.session['log_password'] = pw_hash
                request.session['log_first_name'] = first_name
                request.session['log_last_name'] = last_name
                request.session['log_location'] = location
            else:
                errors['pwconfirm'] = "Passwords did not match!"
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                    return redirect('login:my_register_page')

    return redirect('login:my_successful_log_in')


def successful_log_in(request):
    if request.session['log_email'] == []:
        return redirect('login:my_index')

    else:
        logged_user = User.objects.filter(email=request.session['log_email'])
        user_first_name = logged_user[0].first_name
        user_admin = logged_user[0].admin
        # Category and item stuff to put on the dashboard
        categories_reversed = Category.objects.all().order_by('-id')
        # last 3 items per each last category
        last_category = categories_reversed[0]
        items_reversed_last_cat = last_category.items.all().order_by('-id')
        print(last_category.items.all())
        print(items_reversed_last_cat)
        second_last_category = categories_reversed[1]
        items_reversed_secondlast_cat = second_last_category.items.all().order_by('-id')

        third_last_category = categories_reversed[2]
        items_reversed_thirdlast_cat = third_last_category.items.all().order_by('-id')

        context = {
            "user_first_name": user_first_name,
            "user_admin": user_admin,
            "last_3category": categories_reversed[0:3],
            # SUPER SORRY I DON"T KNOW HOW TO LOOP TO GET THESE! HALP!
            # testing splice .. OMG SLICE WORKS
            "last_cat_last_3items": items_reversed_last_cat[0:3],
            "seclast_cat_last_3items": items_reversed_secondlast_cat[0:3],
            "thirdlast_cat_last_3items": items_reversed_thirdlast_cat[0:3],
            # good golly that was painful...
            "this_user": User.objects.get(email=request.session['log_email']),
        }
        return render(request, "dashboard.html", context)


def direct_message(request):
    context = {
        "this_user": User.objects.get(email=request.session['log_email']),
    }
    return render(request, "direct_message.html", context)


def log_out(request):
    request.session['log_email'] = []
    request.session['log_pw'] = []
    return redirect('login:my_index')


def admin_controls(request):
    this_user = User.objects.get(email=request.session['log_email'])
    if this_user.admin == True:
        # reviews = user.reviews.all()
        # total = 0
        # for review in reviews:
        #     total += int(review.rating)
        # avg = total / len(reviews)
        # new = "%.2f" % avg
        context = {
            "admin": this_user,
            "all_items": Item.objects.all(),
            "all_categories": Category.objects.all(),
            "all_users": User.objects.all()
        }
        return render(request, "admin_controls.html", context)
    else:
        return redirect('login:my_successful_log_in')


def post_new_cat(request):
    if request.method == "POST":
        name = request.POST['name']
        new_category = Category.objects.create(name=name)
        print(new_category)
    return redirect('login:my_admin_controls')


def edit_category(request, category_id):

    context = {
        "this_category": Category.objects.get(id=category_id),
        "admin": User.objects.get(email=request.session['log_email']),
    }
    return render(request, "admin_edit_category.html", context)


def post_edit_category(request, category_id):
    if request.method == "POST":
        this_category = Category.objects.get(id=category_id)
        this_category.name = request.POST['name']
        this_category.save()
    return redirect('login:my_admin_controls')


def delete_category(request, category_id):
    this_category = Category.objects.get(id=category_id)
    this_category.delete()
    return redirect('login:my_admin_controls')


def edit_user(request, user_id):
    context = {
        "edit_user": User.objects.get(id=user_id),
        "admin": User.objects.get(email=request.session['log_email']),
    }
    return render(request, "admin_edit_user.html", context)


def post_edit_user(request, user_id):
    if request.method == "POST":
        this_user = User.objects.get(id=user_id)
        this_user.first_name = request.POST['first_name']
        this_user.last_name = request.POST['last_name']
        this_user.email = request.POST['email']
        this_user.location = request.POST['location']
        this_user.admin = request.POST['admin']
        this_user.save()
        return redirect('login:my_admin_controls')


def delete_user(request, user_id):
    # request.methonggggg
    # if request.method == "POST":
    this_user = User.objects.get(id=user_id)
    this_user.delete()
    return redirect('login:my_admin_controls')
