from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student, Track
from .forms import StudentForm

# rest_framework imports
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# rest_framework views here

@api_view(['GET'])
def api_all_students(request):
    all_students = Student.objects.all()
    serializer = StudentSerializer(all_students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_one_student(request, st_id):
    st = Student.objects.get(id=st_id)
    serializer = StudentSerializer(st, many=False)
    return Response(serializer.data)
    
@api_view(['POST'])
def api_add_student(request):
    st_ser = StudentSerializer(data=request.data)
    if st_ser.is_valid():
        st_ser.save()
        return redirect('api-all')

@api_view(['POST'])
def api_edit_student(request, st_id):
    st = Student.objects.get(id=st_id)
    st_ser = StudentSerializer(instance=st, data=request.data)
    if st_ser.is_valid():
        st_ser.save()
        return redirect('api-all')

@api_view(['DELETE'])
def api_del_student(request, st_id):
    st = Student.objects.get(id=st_id)
    st.delete()
    return Response('Student deleted successfully')


# Create your views here.
def home(request):
    all_students = Student.objects.all()
    context = {'student_list': all_students}
    return render(request, 'djapp/home.html', context)

def show(request, st_id):
    st = Student.objects.get(id=st_id)
    context = {'st': st}
    return render(request, 'djapp/show.html', context)
    
def del_St(request, st_id):
    st = Student.objects.get(id = st_id)
    st.delete()
    return redirect('home')

def addStudent(request):
    st_form = StudentForm()
    if request.method == 'POST':
        st_form = StudentForm(request.POST)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    context = {'st_form': st_form}
    return render(request, 'djapp/add.html', context)

def editStudent(request, st_id):
    st = Student.objects.get(id=st_id)
    st_form = StudentForm(instance=st)
    if request.method == 'POST':
        st_form = StudentForm(request.POST, instance=st)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    context = {'st_form': st_form}
    return render(request, 'djapp/add.html', context)