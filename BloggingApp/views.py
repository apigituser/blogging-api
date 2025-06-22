from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Post
import datetime


@csrf_exempt
def get_create_posts(request):
    if request.method == "GET":
        return getPosts(request)
    elif request.method == "POST":
        return createPost(request)
    else:
        return JsonResponse({"bad request": "invalid http method"}, status=400)
    
def getPosts(request):
    posts = list(Post.objects.values())
    return JsonResponse({"posts": posts})

def createPost(request):
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

@csrf_exempt
def deletePost(request, id):
    if request.method == "DELETE":
        try:
            post = Post.objects.get(id=id)
            Post.delete(post)
            return JsonResponse({"success": "blog deleted successfully"}, status=204)
        except Exception:
            return JsonResponse({"not found": f"post with id {id} not found"}, status=404)
    return JsonResponse({"bad request": "invalid http method"}, status=400)
