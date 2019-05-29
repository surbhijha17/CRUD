from django.shortcuts import render,redirect
from .models import Student
from .forms import Studentform

def CreateStudent(request):
    form=Studentform()
    if request.method == 'POST':
        form = Studentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students:RetrieveAll')
        else:
            form = Studentform()
    #else:
    #    form =Studentform()
    return render(request, 'students/create.html',{'form':form})

def RetrieveAll(request):
    s = Student.objects.all().order_by('-id')
    return render(request, 'students/retall.html', {'s':s})

def Retrieve(request,pk):
    s = Student.objects.get(pk = pk)
    return render(request, 'students/detail.html', {'s':s})
def delete(request,pk):
    s = Student.objects.get(pk = pk).delete()
    return redirect('students:RetrieveAll')

def update(request,pk):
    s = Student.objects.get(pk=pk)
    form = Studentform(instance =s)
    if request.method == 'POST':
        form = Studentform(request.POST, request.FILES, instance=s)
        if form.is_valid():
            form.save()
            return redirect('students:RetrieveAll')
   
    return render(request, 'students/update.html',{'form':form})