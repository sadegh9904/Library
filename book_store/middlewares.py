from typing import Any
from django.shortcuts import redirect
from django.urls import reverse
import re
from django.contrib import messages

class LoginMiddlawere:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):

        print(f"Request Path: {request.path}")  
        print(f"Is Authenticated: {request.user.is_authenticated}")  
        print(f"User: {request.user}")
        pk = "2"
        match = re.search(r"\/(\d+)\/", request.path)
        if match:
            pk = match.group(1)
        checklist = [
            reverse('add-book'),
            reverse('book-list'),
            reverse('edit-book',args=[pk]),
            reverse('delete-book', args=[pk]),


        ]

        customusers = [
            reverse('profile-user'),
            reverse('book-list'),
            reverse('book-borrow', args=[pk]),
        ]

    
        if not request.user.is_superuser and request.path in checklist:
            return redirect('login')
        
        if not request.user.is_authenticated and request.path in customusers:
            messages.error(request, "You should Login first !", "Warning!")
            return redirect('signup')
        
        if request.path == reverse('login'):
            response = self.get_response(request)
            return response


        response = self.get_response(request)

        return response