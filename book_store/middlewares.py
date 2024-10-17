from typing import Any
from django.shortcuts import redirect
from django.urls import reverse
import re

class LoginMiddlawere:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        pk = "4"
        match = "11"
        match = re.search(r"\/(\d+)\/", request.path) #searching int between /  / for example : /11/
        if match:
            pk = match.group(1) #we have just one group :(/d+)


#The list of routes(paths) that only superusrs have access to
        superuser_paths = [
            reverse('add-book'),
            reverse('edit-book',args=[pk]),
            reverse('delete-book', args=[pk]),
        ]


#The list of routes(paths) that only autenticated users have to access
        customuser_paths = [
            reverse('profile-user'),
            reverse('book-borrow', args=[pk]),
        ]


#check if the user isn't a superuser and trying to access superuser_paths ! 
        if not request.user.is_superuser and request.path in superuser_paths:
            return redirect('login')
        

#chek if the user isn't authenticated and tyring to access customuser_paths !        
        if not request.user.is_authenticated and request.path in customuser_paths:
            return redirect('login')


        response = self.get_response(request)

        return response