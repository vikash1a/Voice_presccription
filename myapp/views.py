from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from myapp.models import prescription

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from myapp.forms import prescriptionForm

from datetime import date

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('doctor-profile')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})


class prescriptionCreate(CreateView):
    model = prescription
    form_class = prescriptionForm
    def form_valid(self, form):
        #obj = form.save(commit=False)
        form.instance.doctor = self.request.user
        form.instance.date = date.today()
        return super().form_valid(form)
        #obj.save()

class prescriptionUpdate(UpdateView):
    model = prescription
    form_class = prescriptionForm
    def form_valid(self, form):
        #obj = form.save(commit=False)
        form.instance.date = date.today()
        return super().form_valid(form)
        #obj.save()

class prescriptionDelete(DeleteView):
    model = prescription
    fields = '__all__'



class doctorprofile(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = prescription
    template_name ='myapp/doctor_profile.html'
    paginate_by = 10
    
    def get_queryset(self):
        return prescription.objects.filter(doctor=self.request.user)

class prescriptionDetailView(generic.DetailView):
    model = prescription
    

