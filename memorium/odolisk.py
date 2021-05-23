from django.shortcuts import redirect
def dont_change_pass(request):
    return redirect('posts:index')
