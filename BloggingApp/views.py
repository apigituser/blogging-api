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
    
@csrf_exempt
def get_delete_post(request, id):
    if request.method == "GET":
        return getSinglePost(request, id)
    elif request.method == "DELETE":
        return deletePost(request, id)
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

    return JsonResponse({
        "id": int(post.id),
        "title": title,
        "content": content,
        "category": category,
        "tags": tags.split(","),
        "createdAt": post.createdAt,
        "updatedAt": post.updatedAt
    }, status=201)

def deletePost(request, id):
    try:
        post = Post.objects.get(id=id)
        Post.delete(post)
        return JsonResponse({"success": "blog deleted successfully"}, status=204)
    except Exception:
        return JsonResponse({"not found": f"post with id {id} not found"}, status=404)

def getSinglePost(request, id):
    try:
        post = Post.objects.get(id=id)

        return JsonResponse({
            "id": id,
            "title": post.title,
            "content": post.content,
            "category": post.category,
            "tags": post.tags.split(","),
            "createdAt": post.createdAt,
            "updatedAt": post.updatedAt
        })
    except Exception:
        return JsonResponse({"not found": f"post with id {id} not found"}, status=404)
