from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Post
import datetime

@csrf_exempt
def createPost(request):

    if request.method == "POST":
        try:
            title = request.POST["title"]
            content = request.POST["content"]
            category = request.POST["category"]
            tags = request.POST["tags"]
        except Exception:
            return JsonResponse({"bad request": "provide valid parameters"}, status=400)

        post = Post.objects.create(
            title=title, 
            content=content,
            category=category, 
            tags=tags
        )
        post.save()

        postDate = datetime.datetime.strftime(post.createdAt, format("%Y-%m-%dT%H:%M:%SZ"))

        return JsonResponse({
            "id": int(post.id),
            "title": title,
            "content": content,
            "category": category,
            "tags": tags.split(","),
            "createdAt": postDate,
            "updatedAt": postDate
        }, status=201)
    return JsonResponse({"bad request": "invalid http method"}, status=400)
