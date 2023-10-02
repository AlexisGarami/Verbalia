from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm, GradeForm, PlanForm, PerformanceForm, StudentEntryForm, AttendanceForm, AttendanceEntryForm, GradeAdultForm
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image
from .models import Task, Group, Plan, Performance, Attendance
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.contrib import messages
from django.forms.models import model_to_dict

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')

        except IntegrityError:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'El usuario ya existe!'
            })

        except Exception as e:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': f"Error desconocido: {str(e)}"
            })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden!'
        })


def prueba(request):
    return render(request, 'prueba.html')

@login_required
def tasks(request):
    tasks = Task.objects.filter(user = request.user)

    return render(request, 'tasks.html', {
        'tasks': tasks,
    })

def generate_pdf(grade_instance, request):

    data1 = [['AREA', ' ', 'GRADE EXAM', ' ', 'PERCENTAGE'], [''],
             ['Unit Exam (60%)', ' ---------- ', str(grade_instance.unit_exam_grade),
              ' --------- ', str(grade_instance.unit_exam_porcentage)+'%'], [''],
             ['Speaking (20%)', ' ---------- ', str(grade_instance.speaking_grade),
              ' --------- ', str(grade_instance.speaking_porcentage)+'%'], [''],
             ['Spelling (10%)', ' ---------- ', str(grade_instance.spelling_grade),
              ' --------- ', str(grade_instance.spelling_porcentage)+'%',], [''],
             ['Verbs (10%)', ' ---------- ', str(grade_instance.verbs_grade), ' ---------- ', str(grade_instance.verbs_porcentage)+'%',], ['']]
    

    data2 = [[" ", "STUDENT'S INFORMATION",], [''], [''],
             ["Student's Name: \n\n" + grade_instance.student_name, ' ',
                 'Level:  \n\n' + '       '+grade_instance.level + '        '], [''],
             [' ', 'Unit: ' + grade_instance.unit, ' '], [''],]
  
    imagen_path = "boletas/pdf_images/firma_gabriel.png"  
    firma = Image(imagen_path, width=295, height=125)

    data3 = [['','FINAL AVERAGE: \n\n' + str(grade_instance.total_porcentage/10) + '\n',], 
             ['         ',firma,'']]
    
    path1 = "boletas/pdf_images/LOGO.jpeg"  
    logo1 = Image(path1, width=60, height=55)
    path2 = "boletas/pdf_images/logo2.png"  
    logo2 = Image(path2, width=80, height=50)

    data4 = [[logo1,'                  ', '                          Grades Summary\n\n', '                   ', logo2]]

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="calificaciones_report.pdf"'

    doc = SimpleDocTemplate(response, pagesize=landscape(letter), leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0)


    table1 = Table(data1)
    style1 = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 1), 'cadetblue'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 14),
        ('BACKGROUND', (0, 4), (-1, 5), 'aliceblue'),
        ('BACKGROUND', (0, 8), (-1, 9), 'aliceblue'),
    ])
    table1.setStyle(style1)

    table2 = Table(data2)
    style2 = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 1), 'cadetblue'),
        ('BACKGROUND', (0, 2), (-1, -1), 'aliceblue'),
        ('BACKGROUND', (0, 5), (-1, -1), 'cadetblue'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('TEXTCOLOR', (0, 5), (-1, -1), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTNAME', (0, 5), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 17),
        ('FONTNAME', (0, 2), (-1, -3), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 2), (-1, -3), 16),
    ])
    table2.setStyle(style2)

    table3 = Table(data3)
    style3 = TableStyle([
        ('BACKGROUND', (1, 0), (1,0 ), 'cadetblue'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 14),
        ('GRID', (1, 0), (1, 0), 0.1, 'mintcream'),
        ('GRID', (1, 0), (1, 0), 0.1, 'lightgrey'),
    ])
    table3.setStyle(style3)

    table4 = Table(data4)
    style4 = TableStyle([
        ('TEXTCOLOR', (2, 0), (2,0), 'black'),
        ('ALIGN', (2, 0), (2,0), 'CENTER'),
        ('FONTNAME', (2, 0), (2,0), 'Helvetica-Bold'),
        ('FONTSIZE', (2, 0), (2,0), 19),
        ('TEXTCOLOR', (3, 0), (3,0), 'cadetblue'),
        ('FONTNAME', (3, 0), (3,0), 'Helvetica-Bold'),
        ('FONTSIZE', (3, 0), (3,0), 30),
    ])
    table4.setStyle(style4)

    elements = []
    elements.append(Spacer(0, 4))
    elements.append(table4)
    elements.append(Spacer(0, 5))
    elements.append(table2)
    elements.append(Spacer(0, 10))
    elements.append(table1)
    elements.append(Spacer(0, 5))
    elements.append(table3)

    doc.build(elements)

    return response

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
        'form': TaskForm
    })

    else:
        form = TaskForm(request.POST)
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.save()

        return redirect('tasks')

@login_required
def create_grade_adults(request):
    if request.method == 'POST':
        form = GradeAdultForm(request.POST)
        if form.is_valid():
            grade_instance = form.save()
            return generate_pdf2(grade_instance, request)
    else:
        form = GradeAdultForm()  

    return render(request, 'create_grade_adults.html', {
        'form': form
    })


def generate_pdf2(grade_instance, request):

    data1 = [['AREA', ' ', 'GRADE EXAM', ' ', 'PERCENTAGE'], [''],
             ['Unit Exam (50%)', ' ---------- ', str(grade_instance.unit_exam_grade),
              ' --------- ', str(grade_instance.unit_exam_porcentage)+'%'], [''],
             ['Speaking (20%)', ' ---------- ', str(grade_instance.speaking_grade),
              ' --------- ', str(grade_instance.speaking_porcentage)+'%'], [''],
             ['Spelling (10%)', ' ---------- ', str(grade_instance.spelling_grade),
              ' --------- ', str(grade_instance.spelling_porcentage)+'%',], [''],
             ['Verbs (10%)', ' ---------- ', str(grade_instance.verbs_grade), ' ---------- ', str(grade_instance.verbs_porcentage)+'%',], [''], 
             ['Writing (10%)', ' ---------- ', str(grade_instance.writing_grade), ' ---------- ', str(grade_instance.writing_porcentage)+'%',], ['']]
    

    data2 = [[" ", "STUDENT'S INFORMATION",], [''], [''],
             ["Student's Name: \n\n" + grade_instance.student_name, ' ',
                 'Level:  \n\n' + '       '+grade_instance.level + '        '], [''],
             [' ', 'Unit: ' + grade_instance.unit, ' '], [''],]
  
    imagen_path = "boletas/pdf_images/firma_gabriel.png"  
    firma = Image(imagen_path, width=220, height=100)

    data3 = [['','FINAL AVERAGE: \n' + str(grade_instance.total_porcentage/10) + '\n',], 
             ['         ',firma,'']]
    
    path1 = "boletas/pdf_images/LOGO.jpeg"  
    logo1 = Image(path1, width=60, height=55)
    path2 = "boletas/pdf_images/logo2.png"  
    logo2 = Image(path2, width=80, height=50)

    data4 = [[logo1,'                  ', '                          Grades Summary\n\n', '                   ', logo2]]

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="calificaciones_report.pdf"'

    doc = SimpleDocTemplate(response, pagesize=landscape(letter), leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0)


    table1 = Table(data1)
    style1 = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 1), 'cadetblue'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 14),
        ('BACKGROUND', (0, 4), (-1, 5), 'aliceblue'),
        ('BACKGROUND', (0, 8), (-1, 9), 'aliceblue'),
    ])
    table1.setStyle(style1)

    table2 = Table(data2)
    style2 = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 1), 'cadetblue'),
        ('BACKGROUND', (0, 2), (-1, -1), 'aliceblue'),
        ('BACKGROUND', (0, 5), (-1, -1), 'cadetblue'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('TEXTCOLOR', (0, 5), (-1, -1), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTNAME', (0, 5), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 17),
        ('FONTNAME', (0, 2), (-1, -3), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 2), (-1, -3), 16),
    ])
    table2.setStyle(style2)

    table3 = Table(data3)
    style3 = TableStyle([
        ('BACKGROUND', (1, 0), (1,0 ), 'cadetblue'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 14),
        ('GRID', (1, 0), (1, 0), 0.1, 'mintcream'),
        ('GRID', (1, 0), (1, 0), 0.1, 'lightgrey'),
    ])
    table3.setStyle(style3)

    table4 = Table(data4)
    style4 = TableStyle([
        ('TEXTCOLOR', (2, 0), (2,0), 'black'),
        ('ALIGN', (2, 0), (2,0), 'CENTER'),
        ('FONTNAME', (2, 0), (2,0), 'Helvetica-Bold'),
        ('FONTSIZE', (2, 0), (2,0), 19),
        ('TEXTCOLOR', (3, 0), (3,0), 'cadetblue'),
        ('FONTNAME', (3, 0), (3,0), 'Helvetica-Bold'),
        ('FONTSIZE', (3, 0), (3,0), 30),
    ])
    table4.setStyle(style4)

    elements = []
    elements.append(Spacer(0, 4))
    elements.append(table4)
    elements.append(Spacer(0, 5))
    elements.append(table2)
    elements.append(Spacer(0, 10))
    elements.append(table1)
    elements.append(Spacer(0, 5))
    elements.append(table3)

    doc.build(elements)

    return response


def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade_instance = form.save()
            return generate_pdf(grade_instance, request)
    else:
        form = GradeForm()  

    return render(request, 'create_grade.html', {
        'form': form
    })

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Este usuario no existe! o es incorrecto!'
            })
        else:
            login(request, user)
            return redirect('home')

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'task':task,
            'form': form
        })
    else:
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(request.POST, instance=task)
        form.save()
        return redirect('tasks')
    

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')
    
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    

@login_required
def create_plan(request, group_id):
    # Obtener los datos necesarios
    group = Group.objects.get(pk=group_id)
    user = request.user
    week_start = Plan.get_start_week_date()
    week_end = Plan.get_end_week_date()
    current_week_label = Plan.get_current_week_label()

    # Verifica si esta dentro del plazo acordado
    if not Plan.is_within_deadline():
        messages.error(request, 'El plazo para enviar el plan de esta semana ha terminado. Por favor, vuelva a cargar la página.')
        return redirect('create_plan', group_id=group_id)

    # Se define el formset y las etiquetas asignadas manualmente
    PlanFormSet = formset_factory(PlanForm, extra=5)

    # Si el formulario es enviado
    if request.method == 'POST':
        formset = PlanFormSet(request.POST, prefix='plan')
        if formset.is_valid():    

            #Se itera a través del formset
            for form in formset:

                # Crear el objeto plan sin guardar y asignando los campos fuera del formulario
                plan = form.save(commit=False)
                plan.group = group
                plan.user = user
                plan.creation_week = plan.get_creation_week()
                plan.week_start = week_start
                plan.week_end = week_end

                student_data_list = []
                for entry_form in formset:
                    day = entry_form.cleaned_data.get('day')
                    unit = entry_form.cleaned_data.get('unit')
                    topic = entry_form.cleaned_data.get('topic')
                    clase = entry_form.cleaned_data.get('clase')
                    activities = entry_form.cleaned_data.get('activities')
                    book_pages = entry_form.cleaned_data.get('book_pages')
                    resources = entry_form.cleaned_data.get('resources')
                    expected_learning = entry_form.cleaned_data.get('expected_learning')
                    student_data_list.append({
                        'day':day,
                        'unit':unit,
                        'topic':topic,
                        'clase':clase,
                        'activities':activities,
                        'book_pages':book_pages,
                        'resources':resources,
                        'expected_learning':expected_learning
                    })

                plan.student_data = student_data_list

                plan.save()

                return redirect('inicio_plan')
        
    else:
        formset = PlanFormSet(prefix='plan')

    return render(request, 'create_plan.html', {
        'formset':formset,
        'week_start': week_start,
        'week_end':week_end,
        'editing': False,
        'current_week_label':current_week_label,
        'group':group
    })


def inicio_plan(request):
    user = request.user
    groups = Group.objects.filter(user=user)
    current_week_label = Plan.get_current_week_label()
    

    for group in groups:
        group.plan = group.plan_set.filter(semana=current_week_label).first()

    return render(request, 'inicio_plan.html', {
        'groups':groups
    })


def select_student_count(request, group_id):
    if request.method == 'POST':
        student_count = request.POST.get('student_count')
        return redirect('create_performance', group_id=group_id, student_count=student_count)
    return render(request, 'select_student_count.html', {
        'group_id': group_id
    })


def create_performance(request, group_id, student_count):
    StudentEntryFormSet = formset_factory(StudentEntryForm,  extra=int(student_count))
    group = Group.objects.get(pk=group_id)
    user = request.user
    week_start = Performance.get_start_week_date()
    week_end = Performance.get_end_week_date()
    current_week_label = Performance.get_current_week_label()

    if not Performance.is_within_deadline():
        messages.error(request, 'El plazo para enviar acabo.')
        return redirect(create_performance, group_id=group_id)


    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        formset = StudentEntryFormSet(request.POST, prefix='studententry')

        if form.is_valid() and formset.is_valid():
            performance = form.save(commit=False)
            performance.user = user
            performance.group = group
            performance.creation_week = performance.get_creation_week()
            performance.week_start = week_start
            performance.week_end = week_end


            student_data_list = []
            for entry_form in formset:
                student_name = entry_form.cleaned_data.get('student_name')
                comments = entry_form.cleaned_data.get('comments')
                student_data_list.append({
                    'student_name': student_name,
                    'comments': comments
                })

            performance.student_data = student_data_list
            performance.save()
            
            return redirect('inicio_performance')
        
    else:
        form = PerformanceForm()
        formset = StudentEntryFormSet(prefix='studententry')

    return render(request, 'create_performance.html', {
        'form':form,
        'formset':formset,
        'week_start':week_start,
        'week_end':week_end,
        'editing': False,
        'current_week_label':current_week_label,
        'group':group
    })


def inicio_performance(request):
    user = request.user
    groups = Group.objects.filter(user=user)
    
    current_week_label = Performance.get_current_week_label()

    for group in groups:
        group.performance = group.performance_set.filter(semana=current_week_label).first()

    return render(request, 'inicio_performance.html', {'groups':groups})


def inicio_attendance(request):
    user = request.user
    groups = Group.objects.filter(user=user)

    current_week_label = Attendance.get_current_week_label()
    for group in groups:
        group.attendance = group.attendance_set.filter(semana=current_week_label).first()

    return render(request, 'inicio_attendance.html', {
        'groups':groups
    })


def select_attendance_count(request, group_id):
    if request.method == 'POST':
        student_count = request.POST.get('student_count')
        return redirect('create_attendance', group_id=group_id, student_count=student_count)
    return render(request, 'select_attendance_count.html', {
        'group_id':group_id
    })


def create_attendance(request, group_id, student_count):
    AttendanceEntryFormSet = formset_factory(AttendanceEntryForm, extra=int(student_count))
    user = request.user
    week_start = Performance.get_start_week_date()
    week_end = Performance.get_end_week_date()
    current_week_label = Performance.get_current_week_label()
    group = Group.objects.get(pk=group_id)

    if not Attendance.is_within_deadline():
        messages.error(request, 'El plazo para enviar acabó.')
        return redirect(create_attendance, group_id=group_id)

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        formset = AttendanceEntryFormSet(request.POST, prefix='studententry')

        if form.is_valid() and formset.is_valid():
            attendance = form.save(commit=False)
            attendance.user = user
            attendance.group = group
            attendance.creation_week = attendance.get_creation_week()
            attendance.week_start = week_start
            attendance.week_end = week_end
            attendance.save()

            student_data_list = []
            for entry_form in formset:
                entry = entry_form.save(commit=False)
                entry.attendance = attendance
                entry.save()

                student_name = entry_form.cleaned_data.get('student_name')
                monday = entry_form.cleaned_data.get('monday')
                tuesday = entry_form.cleaned_data.get('tuesday')
                wednesday = entry_form.cleaned_data.get('wednesday')
                thursday = entry_form.cleaned_data.get('thursday')
                friday = entry_form.cleaned_data.get('friday')
                student_data_list.append({
                    'student_name':student_name,
                    'monday':monday,
                    'tuesday':tuesday,
                    'wednesday':wednesday,
                    'thursday':thursday,
                    'friday':friday,
                })

            attendance.student_data = student_data_list
            attendance.save()

            return redirect('inicio_attendance')

    else:
        form = AttendanceForm()
        formset = AttendanceEntryFormSet(prefix='studententry')

    return render(request, 'create_attendance.html', {
        'form':form,
        'formset':formset,
        'week_start': week_start,
        'week_end': week_end,
        'editing':False,
        'current_week_label':current_week_label,
        'group':group
    })


def historical_plans(request, group_id):
    group = Group.objects.get(pk=group_id)
    historical_plans = Plan.objects.filter(group=group).order_by('-week_start')
    return render(request, 'historical_plans.html', {'plans': historical_plans})


def edit_plan(request, week_plan_id):
    #Obteniendo la instancia en cuestion
    plan_instance = get_object_or_404(Plan, id=week_plan_id)
    current_week_label = Plan.get_current_week_label()
    group = plan_instance.group
    # Configurando el Formset

    PlanEntryFormSet = formset_factory(PlanForm, extra=0)

    # Procesando el formset enviado
    if request.method == 'POST':
        formset = PlanEntryFormSet(request.POST, prefix='plan_entry')

        if formset.is_valid():
            student_data_list = []
            for form in formset:
                student_data_list.append(form.cleaned_data)

            plan_instance.student_data = student_data_list
            plan_instance.save()
            
            return redirect('edit_plan', week_plan_id=week_plan_id)
    
    else:
        initial_data = plan_instance.student_data or []
        formset = PlanEntryFormSet(initial=initial_data, prefix='plan_entry',)

        return render(request, 'create_plan.html', {
            'formset':formset,
            'editing': True,
            'current_week_label':current_week_label,
            'group':group
        })


def edit_performance(request, performance_id):
    
    performance_instance = get_object_or_404(Performance, id=performance_id)
    current_week_label = Performance.get_current_week_label()
    StudentEntryFormSet = formset_factory(StudentEntryForm,  extra=0)
    group = performance_instance.group
    
    

    if request.method == 'POST':
        form = PerformanceForm(request.POST, instance=performance_instance)
        formset = StudentEntryFormSet(request.POST, prefix='studententry')

        if form.is_valid() and formset.is_valid():
            performance = form.save(commit=False)

            performance.student_data = [entry.cleaned_data for entry in formset]
            performance.save()

            return redirect('edit_performance', performance_id=performance_id)
        
    else:
        form = PerformanceForm(instance=performance_instance)
        initial_data = performance_instance.student_data
        formset = StudentEntryFormSet(initial=initial_data, prefix='studententry')
        return render(request, 'create_performance.html',{
            'form':form,
            'formset':formset,
            'editing':True,
            'current_week_label':current_week_label,
            'group':group
        })


def edit_attendance(request, attendance_id):
    attendance_instance = get_object_or_404(Attendance, id=attendance_id)
    current_week_label = Attendance.get_current_week_label()
    AttendanceEntryFormSet = formset_factory(AttendanceEntryForm, extra=0)
    group = attendance_instance.group

    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance_instance)
        formset = AttendanceEntryFormSet(request.POST, prefix='studententry')

        if form.is_valid() and formset.is_valid():
            attendance = form.save(commit=False)
            attendance.student_data = [entry.cleaned_data for entry in formset]
            attendance.save()

            return redirect('edit_attendance', attendance_id=attendance_id)
        
    else:
        form = AttendanceForm(instance=attendance_instance)
        initial_data = attendance_instance.student_data
        formset = AttendanceEntryFormSet(initial = initial_data, prefix = 'studententry')
        return render(request, 'create_attendance.html', {
            'form':form,
            'formset':formset,
            'editing': True,
            'current_week_label':current_week_label,
            'group': group
        })


def view_performances(request):
    # Obtener una lista de todas las semanas únicas
    unique_weeks = Performance.objects.values_list('creation_week', flat=True).distinct()

    return render(request, 'view_performances.html', {
        'unique_weeks': unique_weeks
    })


def view_attendances(request):
    unique_weeks = Attendance.objects.values_list('creation_week', flat=True).distinct()

    return render(request, 'view_attendances.html', {
        'unique_weeks': unique_weeks
    })


def view_plans(request):
    unique_weeks = Attendance.objects.values_list('creation_week', flat=True).distinct()

    return render(request, 'view_plans.html', {
        'unique_weeks':unique_weeks
    })


def performance_detail(request, performance_id):
    performance_instance = get_object_or_404(Performance, id=performance_id)
    current_week_label = Performance.get_current_week_label()
    StudentEntryFormSet = formset_factory(StudentEntryForm,  extra=0)
    profesor = performance_instance.user

    if request.method == 'GET':
        form = PerformanceForm(instance=performance_instance)
        initial_data = performance_instance.student_data
        formset = StudentEntryFormSet(initial=initial_data, prefix='studententry')
        return render(request, 'performance_detail.html',{
                'form':form,
                'formset':formset,
                'current_week_label':current_week_label,
                'profesor':profesor,
            })


def attendance_detail(request, attendance_id):
    attendance_instance = get_object_or_404(Attendance, id=attendance_id)
    current_week_label = Attendance.get_current_week_label()
    StudentEntryFormSet = formset_factory(AttendanceEntryForm, extra=0)
    profesor = attendance_instance.user

    if request.method == 'GET':
        form = AttendanceForm(instance=attendance_instance)
        initial_data = attendance_instance.student_data
        formset = StudentEntryFormSet(initial=initial_data, prefix='studententry')
        
        return render(request, 'attendance_detail.html', {
            'form':form,
            'formset':formset,
            'current_week_label':current_week_label,
            'profesor':profesor,
        })
    

def plan_detail(request, plan_id):
    plan_instance = get_object_or_404(Plan, id=plan_id)
    current_week_label = Plan.get_current_week_label()
    PlanEntryFormSet = formset_factory(PlanForm, extra=0)
    profesor = plan_instance.user

    if request.method == 'GET':
        initial_data = plan_instance.student_data
        formset = PlanEntryFormSet(initial=initial_data, prefix='plan_entry')
        form = PlanForm(instance=plan_instance)

        form_data = [getattr(form.instance, field.name) for field in form]

    return render(request, 'plan_detail.html', {
        'formset':formset,
        'form_data':form_data,
        'current_week_label':current_week_label,
        'profesor':profesor,
    })


def performances_for_week(request, week):
    # Obtener todas las performances para una semana especifica
    weekly_performances = Performance.objects.filter(creation_week=week)

    return render(request, 'performances_for_week.html', {
        'weekly_performances':weekly_performances,
        'week':week
    })


def attendances_for_week(request, week):
    # Obtener las attendances para una semana especifica
    weekly_attendances = Attendance.objects.filter(creation_week=week)

    return render(request, 'attendances_for_week.html', {
        'weekly_attendances': weekly_attendances,
        'week': week
    })


def plans_for_week(request, week):
    weekly_plans = Plan.objects.filter(creation_week=week)

    return render(request, 'plans_for_week.html', {
        'weekly_plans':weekly_plans,
        'week':week
    })