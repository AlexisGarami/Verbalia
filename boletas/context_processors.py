from .models import Group

def assignment_check(request):
    if request.user.is_authenticated:
        todos_los_grupos = Group.objects.filter(user=request.user)
        todos_completados = all([group.has_assignment_this_week() for group in todos_los_grupos])

    else:
        todos_completados = False

    return {'todos_completados':todos_completados}


def plan_check(request):
    if request.user.is_authenticated:
        todos_los_grupos = Group.objects.filter(user=request.user)
        plans_completados = all([group.has_plan_this_week() for group in todos_los_grupos])

    else:
        plans_completados = False

    return {'plans_completados':plans_completados}


def performance_check(request):
    if request.user.is_authenticated:
        todos_los_grupos = Group.objects.filter(user=request.user)
        performances_completados = all([group.has_performance_this_week() for group in todos_los_grupos])

    else:
        performances_completados = False

    return {'performances_completados':performances_completados}


def add_permission_info(request):
    can_view_menu = request.user.has_perm('boletas.can_view_menu')

    return {
        'can_view_menu': can_view_menu,
    }
