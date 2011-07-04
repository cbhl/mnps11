# Create your views here.

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect;

from django.contrib.auth.views import password_reset;

from django.contrib.auth.models import User;

from django.contrib.auth import authenticate, login;

def cas_hack_init(request):
    return HttpResponseRedirect('http://www.student.cs.uwaterloo.ca/~m9chang/cgi-bin/mathnews-cas.php');

def cas_hack(request):
    un = request.GET['HTTP_CAS_USER'] # FIXME - one day we will use real CAS
    pw = 'pKSyHwWlbEUvZCAm7jx3MnkRvmi2qzT0Pf0lMGqDI2eHZKIRV4Rj8ipAeEyHapY'
    user_obj = None;
    try:
        user_obj = User.objects.get(username__exact=un);
    except DoesNotExist:
        user_obj = User.objects.create_user(un,'{0}@uwaterloo.ca'.format(un));

    user_obj.is_staff = True;
    user_obj.is_active = True;
    user_obj.is_superuser = True;
    user_obj.set_password(pw);
    user_obj.save()

    user = authenticate(username=un, password=pw)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/admin/')
            #return password_reset(request)
        else:
            # disabled account
            return HttpReponseForbidden()
    else:
        # invalid login
        return HttpResponseNotFound()

