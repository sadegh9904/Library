from typing import Any
from django.shortcuts import redirect
from django.urls import reverse
import re
from django.contrib import messages

class LoginMiddlawere:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        pk = "2"
        match = re.search(r"\/(\d+)\/", request.path)
        if match:
            pk = match.group(1)
        checklist = [
            reverse('book:book-create'),
            reverse('book:book-list'),
            reverse('book:book-update',args=[pk]),
            reverse('book:book-delete', args=[pk]),

            reverse('book:user-profile', args=[pk]),
        ]

        customusers = [
            reverse('book:user-profile'),
            reverse('book:book-borrow', args=[pk]),
        ]

    
        if not request.user.is_superuser and request.path in checklist:
            return redirect('book:login')
        
        if not request.user.is_authenticated and request.path in customusers:
            messages.error(request, "You should Login first !", "Warning!")
            return redirect('book:login')


        response = self.get_response(request)

        return response