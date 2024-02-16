from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta, datetime, time

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CalificacionAdult(models.Model):
    student_name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    unit_exam_grade = models.DecimalField(max_digits=5, decimal_places=2)
    speaking_grade = models.DecimalField(max_digits=5, decimal_places=2)
    spelling_grade = models.DecimalField(max_digits=5, decimal_places=2)
    verbs_grade = models.DecimalField(max_digits=5, decimal_places=2)
    writing_grade = models.DecimalField(max_digits=5, decimal_places=2)
    unit_exam_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    speaking_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    spelling_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    verbs_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    writing_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def final_average(self):
        return (self.unit_exam_grade * 0.5) + (self.speaking_grade * 0.2) + (self.spelling_grade * 0.1) + (self.verbs_grade*0.1) + (self.writing_grade*0.1)
    

    def save(self, *args, **kwargs):
        #Calculando percentage column
        self.unit_exam_porcentage = self.unit_exam_grade * 5
        self.speaking_porcentage = self.speaking_grade * 2
        self.spelling_porcentage = self.spelling_grade * 1
        self.verbs_porcentage = self.verbs_grade * 1
        self.writing_porcentage = self.writing_grade * 1

        #Calcular percentage total
        self.total_porcentage = self.unit_exam_porcentage + self.speaking_porcentage + self.spelling_porcentage + self.verbs_porcentage + self.writing_porcentage

        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.student_name +' Unidad: ' + self.unit


class Calificacion(models.Model):
    student_name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    unit_exam_grade = models.DecimalField(max_digits=5, decimal_places=2)
    speaking_grade = models.DecimalField(max_digits=5, decimal_places=2)
    spelling_grade = models.DecimalField(max_digits=5, decimal_places=2)
    verbs_grade = models.DecimalField(max_digits=5, decimal_places=2)
    unit_exam_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    speaking_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    spelling_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    verbs_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def final_average(self):
        return (self.unit_exam_grade * 0.6) + (self.speaking_grade * 0.2) + (self.spelling_grade * 0.1) + (self.verbs_grade*0.1)
    

    def save(self, *args, **kwargs):
        #Calculando percentage column
        self.unit_exam_porcentage = self.unit_exam_grade * 6
        self.speaking_porcentage = self.speaking_grade * 2
        self.spelling_porcentage = self.spelling_grade * 1
        self.verbs_porcentage = self.verbs_grade * 1

        #Calcular percentage total
        self.total_porcentage = self.unit_exam_porcentage + self.speaking_porcentage + self.spelling_porcentage + self.verbs_porcentage

        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.student_name +' Unidad: ' + self.unit
    

class CalificacionBabies(models.Model):
    student_name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    unit_exam_grade = models.DecimalField(max_digits=5, decimal_places=2)
    speaking_grade = models.DecimalField(max_digits=5, decimal_places=2)
    spelling_grade = models.DecimalField(max_digits=5, decimal_places=2)
    pronunciation_grade = models.DecimalField(max_digits=5, decimal_places=2)
    unit_exam_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    speaking_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    spelling_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pronunciation_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_porcentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def final_average(self):
        return (self.unit_exam_grade * 0.4) + (self.speaking_grade * 0.2) + (self.spelling_grade * 0.2) + (self.pronunciation_grade*0.2)
    

    def save(self, *args, **kwargs):
        #Calculando percentage column
        self.unit_exam_porcentage = self.unit_exam_grade * 4
        self.speaking_porcentage = self.speaking_grade * 2
        self.spelling_porcentage = self.spelling_grade * 2
        self.pronunciation_porcentage = self.pronunciation_grade * 2

        #Calcular percentage total
        self.total_porcentage = self.unit_exam_porcentage + self.speaking_porcentage + self.spelling_porcentage + self.pronunciation_porcentage

        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.student_name +' Unidad: ' + self.unit


class Group(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    schedule = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=True)


    def __str__(self):
        return self.name

    def has_assignment_this_week(self):
        # Obtener las fechas de inicio y fin de la semana actual
        start_of_week = Attendance.get_start_week_date()
        end_of_week = Attendance.get_end_week_date()

        # Ahora, verificamos si hay alguna asignación para este grupo en la semana actual.
        assignments_this_week = self.attendance_set.filter(creation_date__gte=start_of_week, creation_date__lte=end_of_week)

        return assignments_this_week.exists()
    
    def has_plan_this_week(self):
    # Obtener las fechas de inicio y fin de la semana actual
        start_of_week = Plan.get_start_week_date()  # Asumiendo que Plan tiene un método similar
        end_of_week = Plan.get_end_week_date()      # Asumiendo que Plan tiene un método similar

        # Ahora, verificamos si hay algún plan para este grupo en la semana actual.
        plans_this_week = self.plan_set.filter(creation_date__gte=start_of_week, creation_date__lte=end_of_week)

        return plans_this_week.exists()
    
    def has_performance_this_week(self):
        # Obtener las fechas de inicio y fin de la semana actual
        start_of_week = Performance.get_start_week_date()  # Asumiendo que Performance tiene un método similar
        end_of_week = Performance.get_end_week_date()      # Asumiendo que Performance tiene un método similar

        # Ahora, verificamos si hay alguna actuación para este grupo en la semana actual.
        performances_this_week = self.performance_set.filter(creation_date__gte=start_of_week, creation_date__lte=end_of_week)

        return performances_this_week.exists()


class Plan(models.Model):
    DAY_CHOICES = [
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday')
    ]

    day = models.CharField(
        max_length=10,
        choices=DAY_CHOICES,
        null=True, 
        blank=True
    )
    topic = models.CharField(max_length=100, null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    clase = models.CharField(max_length=50, null=True, blank=True)
    semana = models.CharField(max_length=50, null=True, blank=True)
    activities = models.TextField(max_length=800, null=True, blank=True)
    book_pages = models.TextField(max_length=200, null=True, blank=True)
    resources = models.TextField(max_length=800, null=True, blank=True)
    expected_learning = models.TextField(max_length=800, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True)
    is_submitted = models.BooleanField(default=False)
    week_number = models.PositiveIntegerField(null=True, blank=True)
    week_start = models.DateField(null=True)
    week_end = models.DateField(null=True)
    student_data = models.JSONField(blank=True, null=True)
    creation_week = models.CharField(max_length=50, null=True)



    def __str__(self):
        formatted_date = self.creation_date.astimezone(timezone.get_current_timezone()).strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.group.name}, Plan: {formatted_date}, Teacher: {self.user}"
    
    @staticmethod
    def is_within_deadline():
        """ Comprueba si la fecha y hora actual está dentro del plazo de la semana actual """
        now = timezone.localtime(timezone.now())
        # Obtener el próximo sábado
        next_saturday = now + timedelta((5-now.weekday()) % 7)
        # Establecer la hora a las 5 pm
        deadline_time = next_saturday.replace(hour=17, minute=0, second=0, microsecond=0)
        return now <= deadline_time
    
    def save(self, *args, **kwargs):
        if not self.semana:
            self.semana = self.calculate_week_label()  
        super().save(*args, **kwargs)

    @staticmethod
    def get_start_week_date(today=None):
        if not today:
            today = timezone.localtime(timezone.now())

        # Determinar el último sábado a las 5:01 pm
        if today.weekday() == 5 and today.time() >= time(17,1):  
            return datetime.combine(today.date(), time(17, 1))

        # Si es sábado pero antes de las 5:01 pm
        elif today.weekday() == 5 and today.time() < time(17,1):
            last_saturday = today - timedelta(weeks=1)
            return datetime.combine(last_saturday, time(17, 1))

        # Para cualquier otro día (de domingo a viernes)
        else:
            last_saturday = today - timedelta(days=(today.weekday() - 5) % 7)
            return datetime.combine(last_saturday, time(17, 1))
        

    @staticmethod
    def get_end_week_date(today=None):
        if not today:
            today = timezone.localtime(timezone.now())
        start_week_date = Plan.get_start_week_date(today)
        return start_week_date + timedelta(days=7)- timedelta(minutes=1)
    
    @staticmethod
    def get_current_week_label():
        today = timezone.localtime(timezone.now())
        start_week_datetime = Plan.get_start_week_date(today)
        end_week_datetime = Plan.get_end_week_date(start_week_datetime)

        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        if start_week_datetime.month != end_week_datetime.month:
            label = "{} {} - {} {}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, month_names[end_week_datetime.month - 1], end_week_datetime.day)
        else:
            label = "{} {}-{}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, end_week_datetime.day)

        return label

    def calculate_week_label(self):
        return self.get_current_week_label()
    
    def get_creation_week(self):
        creation = self.creation_date
        start_week_datetime = Performance.get_start_week_date(creation)
        end_week_datetime = Performance.get_end_week_date(start_week_datetime)

        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        if start_week_datetime.month != end_week_datetime.month:
            label = "{} {} - {} {}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, month_names[end_week_datetime.month - 1], end_week_datetime.day)
        else:
            label = "{} {}-{}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, end_week_datetime.day)

        return label
    
    
class Performance(models.Model):
    semana = models.CharField(max_length=60, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True)
    is_submitted = models.BooleanField(default=False)
    week_number = models.PositiveIntegerField(null=True, blank=True)
    week_start = models.DateField(null=True)
    week_end = models.DateField(null=True)
    student_data = models.JSONField(blank=True, null=True)
    creation_week = models.CharField(max_length=50, null=True)

    def __str__(self):
        formatted_date = self.creation_date.astimezone(timezone.get_current_timezone()).strftime("%Y-%m-%d %H:%M:%S")
        group_name = self.group.name if self.group else "No Group"
        return f"{group_name}, Performance: {formatted_date}, Teacher: {self.user}"
    

    @staticmethod
    def is_within_deadline():
        """ Comprueba si la fecha y hora actual está dentro del plazo de la semana actual """
        now = timezone.now()
        # Obtener el próximo sábado
        next_saturday = now + timedelta((5-now.weekday()) % 7)
        # Establecer la hora a las 5 pm
        deadline_time = next_saturday.replace(hour=17, minute=0, second=0, microsecond=0)
        return now <= deadline_time
    
    def save(self, *args, **kwargs):
        if not self.semana:
            self.semana = self.calculate_week_label()  
        super().save(*args, **kwargs)


    @staticmethod
    def get_start_week_date(today=None):
        if not today:
            today = timezone.localtime(timezone.now())

        # Determinar el último sábado a las 5:01 pm
        if today.weekday() == 5 and today.time() >= time(17,1):  
            return datetime.combine(today.date(), time(17, 1))

        # Si es sábado pero antes de las 5:01 pm
        elif today.weekday() == 5 and today.time() < time(17,1):
            last_saturday = today - timedelta(weeks=1)
            return datetime.combine(last_saturday, time(17, 1))

        # Para cualquier otro día (de domingo a viernes)
        else:
            last_saturday = today - timedelta(days=(today.weekday() - 5) % 7)
            return datetime.combine(last_saturday, time(17, 1))
        

    @staticmethod
    def get_end_week_date(today=None):
        if not today:
            today = timezone.localtime(timezone.now())
        start_week_date = Attendance.get_start_week_date(today)
        return start_week_date + timedelta(days=7) - timedelta(minutes=1)
    

    @staticmethod
    def get_current_week_label():
        today = timezone.localtime(timezone.now())
        start_week_datetime = Attendance.get_start_week_date(today)
        end_week_datetime = Attendance.get_end_week_date(start_week_datetime)

        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        if start_week_datetime.month != end_week_datetime.month:
            label = "{} {} - {} {}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, month_names[end_week_datetime.month - 1], end_week_datetime.day)
        else:
            label = "{} {} - {}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, end_week_datetime.day)

        return label
    
    def calculate_week_label(self):
        return self.get_current_week_label()


    def get_creation_week(self):
        creation = self.creation_date
        start_week_datetime = Performance.get_start_week_date(creation)
        end_week_datetime = Performance.get_end_week_date(start_week_datetime)

        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        if start_week_datetime.month != end_week_datetime.month:
            label = "{} {} - {} {}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, month_names[end_week_datetime.month - 1], end_week_datetime.day)
        else:
            label = "{} Semana: {}-{}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, end_week_datetime.day)

        return label
    

class StudentEntry(models.Model):
    student_name = models.CharField(max_length=60, null=True, blank=True)
    comments = models.TextField(max_length=600, null=True, blank=True)
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, related_name='entries')


class Attendance(models.Model):
    semana = models.CharField(max_length=60)
    creation_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True)
    is_submitted = models.BooleanField(default=False)
    week_number = models.PositiveIntegerField(null=True, blank=True)
    week_start = models.DateField(null=True)
    week_end = models.DateField(null=True)
    student_data = models.JSONField(blank=True, null=True)
    creation_week = models.CharField(max_length=50, null=True)

    def __str__(self):
        formatted_date = self.creation_date.astimezone(timezone.get_current_timezone()).strftime("%Y-%m-%d %H:%M:%S")
        group_name = self.group.name if self.group else "No Group"
        return f"{group_name}, Attendance: {formatted_date}, Teacher: {self.user}"
    

    @staticmethod
    def is_within_deadline():
        """ Comprueba si la fecha y hora actual está dentro del plazo de la semana actual """
        now = timezone.localtime(timezone.now())
        # Obtener el próximo sábado
        next_saturday = now + timedelta((5-now.weekday()) % 7)
        # Establecer la hora a las 5 pm
        deadline_time = next_saturday.replace(hour=17, minute=0, second=0, microsecond=0)
        print("Now:", now)
        print("Deadline:", deadline_time)
        return now <= deadline_time
    
    def save(self, *args, **kwargs):
        """Extiende la funcionalidad del metodo save() asignando el la etiqueta de week_label a el campo semana"""
        if not self.semana:
            self.semana = self.calculate_week_label()  
        super().save(*args, **kwargs)


    @staticmethod
    def get_start_week_date(today=None):
        if not today:
            today = timezone.localtime(timezone.now())

        # Determinar el último sábado a las 5:01 pm
        if today.weekday() == 5 and today.time() >= time(17,1):  
            return datetime.combine(today.date(), time(17, 1))

        # Si es sábado pero antes de las 5:01 pm
        elif today.weekday() == 5 and today.time() < time(17,1):
            last_saturday = today - timedelta(weeks=1)
            return datetime.combine(last_saturday, time(17, 1))

        # Para cualquier otro día (de domingo a viernes)
        else:
            last_saturday = today - timedelta(days=(today.weekday() - 5) % 7)
            return datetime.combine(last_saturday, time(17, 1))
        

    @staticmethod
    def get_end_week_date(today=None):
        if not today:
            today = timezone.localtime(timezone.now())
        start_week_date = Attendance.get_start_week_date(today)
        return start_week_date + timedelta(days=7) - timedelta(minutes=1)
    

    @staticmethod
    def get_current_week_label():
        today = timezone.localtime(timezone.now())
        start_week_datetime = Attendance.get_start_week_date(today)
        end_week_datetime = Attendance.get_end_week_date(start_week_datetime)

        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        if start_week_datetime.month != end_week_datetime.month:
            label = "{} {} - {} {}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, month_names[end_week_datetime.month - 1], end_week_datetime.day)
        else:
            label = "{} {} - {}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, end_week_datetime.day)

        return label
    
    def calculate_week_label(self):
        return self.get_current_week_label()


    def get_creation_week(self):
        creation = self.creation_date
        start_week_datetime = Performance.get_start_week_date(creation)
        end_week_datetime = Performance.get_end_week_date(start_week_datetime)

        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        if start_week_datetime.month != end_week_datetime.month:
            label = "{} {} - {} {}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, month_names[end_week_datetime.month - 1], end_week_datetime.day)
        else:
            label = "{} {} - {}".format(month_names[start_week_datetime.month - 1], start_week_datetime.day, end_week_datetime.day)

        return label


class AttendanceEntry(models.Model):
    student_name = models.CharField(max_length=60, null=True, blank=True)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='entries', null=True, blank=True)
    monday = models.CharField(max_length=1, null=True, blank=True)
    tuesday = models.CharField(max_length=1, null=True, blank=True)
    wednesday = models.CharField(max_length=1, null=True, blank=True)
    thursday = models.CharField(max_length=1, null=True, blank=True)
    friday = models.CharField(max_length=1, null=True, blank=True)


class ResponsibilityNote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Relación uno a uno con User
    note = models.CharField(max_length=255) # Nota o comentario

    def __str__(self):
        return f"{self.user.username} - {self.note}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

class FeedbackNote(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return f"{self.user.username} - Feedback"
    
class MenuPermissions(models.Model):
    class Meta:
        managed = False  # No se crea una tabla en la base de datos para este modelo
        default_permissions = ()
        permissions = (
            ("can_view_menu", "Puede ver el menú"),
        )
