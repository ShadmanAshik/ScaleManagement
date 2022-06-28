from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from accesscontrol.forms import *
from vwm_master.decorators import admin_only






## PROFILE
def profile(request):
    return render(request, 'accesscontrol/profile.html')




## LOGIN
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)    
            return redirect('home')
            

        else:
            messages.error(request,'User name or password is incorrect.')
            

    context = {}
    return render(request, 'accesscontrol/login.html',context)


## LOGOUT
def logout_user(request):
    logout(request)
    return redirect('login')



########################################################################################################
## USER ADMINISTRATION
########################################################################################################

## USER GROUP
@admin_only
def viewusergroups(request):
    headerText = 'User Groups'
    createData = 'createusergroup'


    groups = Group.objects.all()

    context = {
        'headerText' : headerText,
        'groups' : groups,
        'createData' : createData,
    }
    return render(request, 'accesscontrol/accessview.html', context)


@admin_only
def creategroup(request):
    headerText = 'Uesr Group'
    

    if request.method == 'POST':        
        try:
            userGroup = request.POST.get('strGroupName')
            data = Group.objects.create(name = userGroup)
            data.save()
            return redirect('viewusergroups') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {        
        'headerText' : headerText,
    }
    return render(request, 'accesscontrol/accessentry.html', context)


@admin_only
def assignusergroups(request, varID):
    headerText = 'Add User to Groups'

    groups = Group.objects.get(id= varID)

    users = User.objects.all()

    if request.method == 'POST':
        userName = request.POST.get('username')
        userId = User.objects.get(username = userName)
        groups.user_set.add(userId)
        return redirect('viewuser')

    context = {
        'headerText' : headerText,
        'groups' : groups,
        'users' : users,
    }
    return render(request, 'accesscontrol/accessentry.html', context)





@admin_only
def viewuser(request):
    headerText = 'Users'
    createData = 'createuser'

    users = User.objects.all()

    context = {
        'headerText' : headerText,
        'createData' : createData,
        'users' : users,
    }
    return render(request, 'accesscontrol/accessview.html', context)


@admin_only
def createuser(request):
    headerText = 'Users'
    groups = Group.objects.all()

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()            
            uname = form.cleaned_data.get('username')  

            ## added 4-Nov-21
            groupName = request.POST.get('groupname')
            if groupName != 'No Group':
                groups = Group.objects.get(name = groupName) 
                userId = User.objects.get(username = uname)
                groups.user_set.add(userId.id)   

            ## Redirect to the profile create page based on user type
            userType = request.POST.get('usertype')

            if userType == 'Merchant':
                return redirect('createcustomerwithuser', varUser = uname)     
            elif userType == 'Rider':
                return redirect('createriderwithuser', varUser = uname)
            else:
                return redirect('viewuser')        
        
    context = {
        'headerText' : headerText,
        'form': form,
        'groups' : groups,
        }
    return render(request, 'accesscontrol/accessentry.html', context)


@admin_only
def edituser(request, varCode):
    headerText = 'Users'

    user = User.objects.get(id = varCode)

    groups = Group.objects.all()

    form = EditUserForm(instance = user)

    if request.method == "POST":
        form = EditUserForm(request.POST, instance = user)

        if form.is_valid():
            user = form.save()            
            uname = form.cleaned_data.get('username')           

            return redirect('viewuser')        
        
    context = {
        'headerText' : headerText,
        'form': form,
        'groups' : groups,
        }
    return render(request, 'accesscontrol/accessentry.html', context)



@admin_only
def resetpassword(request, vUser):
    headerText = 'Re-set Password'
    createButton = 'No'

    user = User.objects.get(id = vUser)

    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Re-entered password not matched")
        else:
            try:
                user.set_password(password1)
                user.save()
                #messages.success(request, "Re-set password completed successfully.")
                return redirect('viewuser')
            except Exception as e:
                messages.error(request, str(e))


    context = {
        'headerText' : headerText,
        'createButton' : createButton,
    }
    return render(request, 'accesscontrol/accessentry.html', context)



@login_required(login_url='login')
def changepassword(request):
    headerText = 'Change Password'

    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password changed successfully.')
            return redirect('home')
        
    else:
        form = ChangePasswordForm(request.user)

    context = {
        'form' : form,
        'headerText' : headerText,
    }  
    return render(request, 'accesscontrol/accessentry.html', context)