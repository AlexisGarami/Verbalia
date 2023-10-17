from .models import Group


def check_assignments_for_user(user):
    # Obtenemos todos los grupos asociados a ese usuario.
    todos_los_grupos = Group.objects.filter(user=user)
    # Comprobamos si todos los grupos han completado su tarea esta semana.
    todos_completados = all([group.has_assignment_this_week() for group in todos_los_grupos])
    
    return todos_completados

def check_plans_for_user(user):
    # Obtenemos todos los grupos asociados a ese usuario.
    todos_los_grupos = Group.objects.filter(user=user)
    # Comprobamos si todos los grupos han completado su tarea esta semana.
    todos_completados = all([group.has_plan_this_week() for group in todos_los_grupos])
    
    return todos_completados


def check_performances_for_user(user):
    # Obtenemos todos los grupos asociados a ese usuario.
    todos_los_grupos = Group.objects.filter(user=user)
    # Comprobamos si todos los grupos han completado su tarea esta semana.
    todos_completados = all([group.has_performance_this_week() for group in todos_los_grupos])
    
    return todos_completados

