from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from instrument.models import numOfYear, numOfMonth, numOfDay, numOfTime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
def index(request):
	today = datetime.date.today()
	one_day = datetime.timedelta(days=30)
	showDate = today

	firstDayOfMonth = datetime.date(showDate.year, showDate.month, 1)
	m = numOfMonth.objects.get(number=firstDayOfMonth.month-1)
	weekday = firstDayOfMonth.weekday() + 2
	if weekday > 6:
		weekday = firstDayOfMonth.weekday() - 5

	outWeek0 = [0]*7
	outWeek1 = [0]*7
	outWeek2 = [0]*7
	outWeek3 = [0]*7
	outWeek4 = [0]*7
	outWeek5 = [0]*7
	count = 1
	for x in range(weekday,7):
		outWeek0[x] = count
		count = count + 1

	for x in range(0,7):
		outWeek1[x] = count
		count = count + 1

	for x in range(0,7):
		outWeek2[x] = count
		count = count + 1

	for x in range(0,7):
		outWeek3[x] = count
		count = count + 1

	for x in range(0,7):
		outWeek4[x] = count
		count = count + 1
		if count > m.numberOfDays:
			break

	for x in range(0,7):
		if count > m.numberOfDays:
			break
		outWeek5[x] = count
		count = count + 1


	context_dict = {'year':showDate.year, 'month': m, 'day': showDate.day, 'outWeek0': outWeek0, 
		'outWeek1': outWeek1, 'outWeek2': outWeek2, 'outWeek3': outWeek3, 'outWeek4': outWeek4, 'outWeek5': outWeek5}
	#return HttpResponse(showDate)

	response = render(request,'instrument/index.html', context_dict)

	return response


def dayShow(request, number_of_year, number_of_month, number_of_day):
    context_dict = {}
    # showDate = datetime.date.today()
     

    # firstDayOfMonth = datetime.date(showDate.year, showDate.month, 1)
    m = numOfMonth.objects.get(name=number_of_month)

    try:
        dateOfMonth = numOfDay.objects.get(number=number_of_day, numofmonth=m)
        context_dict['dateOfMonth'] = dateOfMonth

    except numOfDay.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    return render(request, 'instrument/show.html', context_dict)

# def register(request):

#      # A boolean value for telling the template whether the registration was successful.
#     # Set to False initially. Code changes value to True when registration succeeds.
#     registered = False

#     # If it's a HTTP POST, we're interested in processing form data.
#     if request.method == 'POST':
#         # Attempt to grab information from the raw form information.
#         # Note that we make use of both UserForm and UserProfileForm.
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)

#         # If the two forms are valid...
#         if user_form.is_valid() and profile_form.is_valid():
#             # Save the user's form data to the database.
#             user = user_form.save()

#             # Now we hash the password with the set_password method.
#             # Once hashed, we can update the user object.
#             user.set_password(user.password)
#             user.save()

#             # Now sort out the UserProfile instance.
#             # Since we need to set the user attribute ourselves, we set commit=False.
#             # This delays saving the model until we're ready to avoid integrity problems.
#             profile = profile_form.save(commit=False)
#             profile.user = user

#             # Did the user provide a profile picture?
#             # If so, we need to get it from the input form and put it in the UserProfile model.
#             if 'picture' in request.FILES:
#                 profile.picture = request.FILES['picture']

#             # Now we save the UserProfile model instance.
#             profile.save()

#             # Update our variable to tell the template registration was successful.
#             registered = True

#         # Invalid form or forms - mistakes or something else?
#         # Print problems to the terminal.
#         # They'll also be shown to the user.
#         else:
#             print user_form.errors, profile_form.errors

#     # Not a HTTP POST, so we render our form using two ModelForm instances.
#     # These forms will be blank, ready for user input.
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()

#     # Render the template depending on the context.
#     return render(request,
#             'instrument/register.html',
#             {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


@login_required
def add_time(request, day):

    try:
        cat = numOfTime.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form':form, 'category': cat, 'category_name_slug': category_name_slug}

    return render(request, 'instrument/add_time.html', context_dict)



def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/instrument/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'instrument/login.html', {})

@login_required
def restricted(request):
    return render(request, 'instrument/restricted.html', {})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/instrument/')