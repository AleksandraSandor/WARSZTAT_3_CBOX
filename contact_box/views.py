from contact_box.models import Address, Person, Phone, Email, Group
from contact_box.forms import PostForm, FormsForm, PhoneForm, EmailForm, AddressForm, GroupForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def new_person(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('show_person', id=post.id)
    else:
        form = PostForm()
        msg_add = "Add new person:"
    return render(request, 'contact_box/add.html', {"msg_add": msg_add, 'form': form})


def all_people(request):
    persons = Person.objects.all().order_by('name')
    return render(request, 'contact_box/all_people.html', {'persons': persons, 'form': True})


def show_person(request, id):
    person = get_object_or_404(Person, pk=id)
    phones = Phone.objects.filter(persons_id=id)
    emails = Email.objects.filter(persons_id=id)
    address = Address.objects.filter(id=person.address_id)
    groups = Group.objects.filter(persons = id)
    return render(request, 'contact_box/single_person.html',
                  {'person': person, 'phones': phones, 'emails': emails, 'address': address, 'groups': groups})


def modify_person(request, id):
    post = get_object_or_404(Person, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_people')
    else:
        form = PostForm(instance=post)
        msg_edit = "Zedytuj kontakt:"
    return render(request, 'contact_box/modify.html', {"msg_edit": msg_edit, 'form': form, 'room': post})


def delete_person(request, id):
    person_delete = Person.objects.get(pk=id)
    person_delete.delete()
    return render(request, 'contact_box/delete.html', {"person_delete": person_delete})


def all_address(request):
    address = Address.objects.all()
    return render(request, 'contact_box/all_address.html', {'address': address, 'form': True})


def add_address(request):
    if request.method == "POST":
        form = FormsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_address')
    else:
        form = FormsForm()
        msg_add = "Add new address:"
    return render(request, 'contact_box/add.html', {"msg_add": msg_add, 'form': form})


def edit_address(request, id):
    post = get_object_or_404(Address, pk=id)
    if request.method == "POST":
        form = FormsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_address')
    else:
        form = FormsForm(instance=post)
        msg_edit = "Edit address:"
    return render(request, 'contact_box/address_modify.html', {"msg_edit": msg_edit, 'form': form, 'room': post})


def delete_address(request, id):
    address_delete = Address.objects.get(pk=id)
    address_delete.delete()
    return render(request, 'contact_box/address_delete.html')


def select_address(request, id):
    post = get_object_or_404(Person, pk=id)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.id = id
            post.save()
            return redirect('show_person', id=id)
    else:
        form = AddressForm()
    return render(request, 'contact_box/add.html', {'form': form, 'id': id})


def add_email(request, id):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.persons_id = id
            post.save()
            return redirect('show_person', id=id)
    else:
        form = EmailForm()
    return render(request, 'contact_box/add.html', {'form': form, 'id': id})


def add_phone(request, id):
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.persons_id = id
            post.save()
            return redirect('show_person', id=id)
    else:
        form = PhoneForm()
    return render(request, 'contact_box/add.html', {'form': form, 'id': id})


def delete_email(request, id):
    email_delete = Email.objects.get(id=id)
    person = email_delete.persons_id
    email_delete.delete()
    return redirect('show_person', id=person)


def delete_phone(request, id):
    phone_delete = Phone.objects.get(id=id)
    person = phone_delete.persons_id
    phone_delete.delete()
    return redirect('show_person', id=person)


def delete_person_address(request, id):
    person = Person.objects.get(id=id)
    person.address_id = None
    person.save()
    return redirect('show_person', id=id)


def all_groups(request):
    groups = Group.objects.all().order_by('title')
    return render(request, 'contact_box/all_groups.html', {'groups': groups, 'form': True})


def group_add(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()
            return redirect('all_groups')
    else:
        form = GroupForm()
    return render(request, 'contact_box/add.html', {'form': form})

def edit_group(request, id):
    post = get_object_or_404(Group, pk=id)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()
            return redirect('all_groups')
    else:
        form = GroupForm(instance=post)
        msg_edit = "Edit group:"
    return render(request, 'contact_box/group_modify.html', {"msg_edit": msg_edit, 'form': form, 'room': post})


def delete_group(request, id):
    group_delete = Group.objects.get(pk=id)
    group_delete.delete()
    return render(request, 'contact_box/group_delete.html')

def group_detail(request, id):
    group = get_object_or_404(Group, pk=id)
    return render(request, 'contact_box/single_group.html',
                  {'group': group})


def group_search(request):
    if request.method == "POST":
        contact_name = request.POST.get("member")
        contacts = Person.objects.filter(name__icontains=contact_name) | Person.objects.filter(surname__icontains=contact_name)
        groups = None
        if contacts:
            groups = contacts[0].group.all()
        else:
            groups = ""
        context = {"groups": groups}
        return render(request, "contact_box/search_members.html", context)
    else:
        return render(request, "contact_box/search_members.html")


