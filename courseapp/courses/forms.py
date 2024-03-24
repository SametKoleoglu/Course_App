from sqlite3 import Date
from django import forms
from django.forms import TextInput, Textarea, SelectMultiple, CheckboxInput,DateInput

from courses.models import Course


# class CourseForm(forms.Form):
#     title = forms.CharField(label="Course Title", max_length=50,
#                             widget=forms.TextInput(attrs={"class": "form-control"}))

#     description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     date = forms.DateField(widget=forms.TextInput(attrs={"class": "form-control","type":"date","value": Date.today()}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     isActive = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),required=False)
#     isHome = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),required=False)

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels = {
            "title": "Course Title",
            "description": "Description",
            "slug": "Slug",
            "isActive": "Active",
            "isHome": "Home",
            "categories": "Categories"
        }
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control"}),
            "isActive": CheckboxInput(attrs={"class": "form-check-input"}),
            "isHome": CheckboxInput(attrs={"class": "form-check-input"}),
            "categories": SelectMultiple(attrs={"class": "form-select"})
        }
        error_messages = {
            "title": {"required": "Please enter a title", "max_length": "Title must be less than 50 characters"},
            "description": {"required": "Please enter a description"},
            "date": {"required": "Please enter a date"},
            "slug": {"required": "Please enter a slug"},
            "categories": {"required": "Please select a category"}
        }


class CourseEdit(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels = {
            "title": "Course Title",
            "description": "Description",
            "slug": "Slug",
            "isActive": "Active",
            "isHome": "Home",
            "categories": "Categories"
        }
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control"}),
            "slug": TextInput(attrs={"class": "form-control"}),
            "isActive": CheckboxInput(attrs={"class": "form-check-input"}),
            "isHome": CheckboxInput(attrs={"class": "form-check-input"}),
            "categories": SelectMultiple(attrs={"class": "form-select"})
        }
        error_messages = {
            "title": {"required": "Please enter a title", "max_length": "Title must be less than 50 characters"},
            "description": {"required": "Please enter a description"},
            "date": {"required": "Please enter a date"},
            "slug": {"required": "Please enter a slug"},
            "categories": {"required": "Please select a category"}
        }

class UploadForm(forms.Form):
    # images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    image = forms.ImageField()