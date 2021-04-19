from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def main(request):
    return render(request,'index.html')

def form_submit(request):
    request.session['name_from_form'] = request.POST['fname']
    request.session['location_from_form'] = request.POST['location']
    request.session['language_from_form'] = request.POST['language']
    request.session['comment_from_form'] = request.POST['comment']
    # first_from_form = request.POST['first']
    return redirect('/result')

def result(request):
    context = {
    	"name_on_template" : request.session['name_from_form'],
    	"location_on_template" : request.session['location_from_form'],
        "language_on_template" : request.session['language_from_form'],
        "comment_on_template" : request.session['comment_from_form'],
        # "first_on_template" : first_from_form
    }
    return render(request, 'result.html', context)

