from django import forms

from .models import Post
	#tell Django that the form is a ModelForm, which is built in
class PostForm(forms.ModelForm):

	class Meta:
		#tells django which model to use to create the form 'Post'
		model = Post
		fields = ('title', 'text',)