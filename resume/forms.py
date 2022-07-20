from django import forms


class resumedata(forms.Form):
        firstname=forms.CharField(label="First Name")
        lastname=forms.CharField(label="Last Name")
        Dob=forms.DateField(label="D.O.B")
        email=forms.EmailField(label="Email-id")
        image=forms.ImageField(label="Uplode image")
        File=forms.FileField(label="Upload CV")

