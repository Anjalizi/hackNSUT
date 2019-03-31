from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				# checking is username already exists
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error': 'This username has already been taken'})
			except User.DoesNotExist:
				# logging in as the user
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				login(request, user)
				return render(request, 'accounts/login.html')

		else:
			return render(request, 'accounts/signup.html', {'error': 'Passwords did not match'})

	else:
		return render(request, 'accounts/signup.html')

# how to log a user in : documentation
def loginview(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request, 'gesture/index.html', {'error': 'Logged in successfully'})
		else:
			return render(request, 'accounts/login.html', {'error': 'Invalid username/password. Try again.'})
	else:
		return render(request, 'accounts/login.html')

