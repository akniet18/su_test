from django import forms
from django.contrib import admin
from .models import User, HistoryModel
from django.contrib.auth.forms import UserChangeForm,AdminPasswordChangeForm

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username','password',"first_name", "last_name", 'is_staff', 'is_superuser',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class AuthorAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    change_password_form = AdminPasswordChangeForm
    list_display = ["username", "first_name", "last_name", "card_id"]


admin.site.register(User, AuthorAdmin)
admin.site.register(HistoryModel)

