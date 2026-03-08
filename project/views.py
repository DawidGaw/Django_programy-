from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from .models import Bug, Project, User


@require_http_methods(["GET"])
def bugs(request):
    project_id = request.GET.get("project_id")
    user_id = request.GET.get("user_id")

    if not project_id and not user_id:
        return JsonResponse({"error": "Project or user id is required"}, status=400)

    filters ={}

    if project_id:
        try:
            project = Project.objects.get(id=project_id)
            filters["project"] = project
        except Project.DoesNotExist:
            return JsonResponse({"error": "Project does not exist"}, status=404)

    if user_id:
        try:
            user = User.objects.get(id=user_id)
            filters["user"] = user
        except User.DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=404)

    bugs = Bug.objects.filter(**filters)
    bugs_data = [
        {
            "id": bug.id,
            "description": bug.description,
            "username": bug.user.username,
            "project": bug.project.name,
        }
        for bug in bugs
    ]
    return JsonResponse({"bugs": bugs_data}, status=200)







