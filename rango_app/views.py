from django.shortcuts import render
from rango_app.models import Category, Page
from rango_app.forms import CategoryForm, PageForm


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'pageViews': page_list}

    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')


def category(request, category_name_slug):
    context_dict = {}

    try:
        category_obj = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category_obj.name
        context_dict['category_slug_name'] = category_name_slug

        pages = Page.objects.filter(category=category_obj)

        context_dict['pages'] = pages
        context_dict['category'] = category_obj
    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad from (or form details), no form supplied...
    # Render the from with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form':form, 'category': cat, 'slug': category_name_slug}

    return render(request, 'rango/category/add_page.html', context_dict)


def page_not_found(request):
    context_dict = {'page_name': request.path}

    return render(request, 'rango/page_not_found.html', context_dict)