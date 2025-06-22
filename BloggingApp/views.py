from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Post

@csrf_exempt
def createPost(request):
    if request.method == "POST":
        title = "Test Title"
        content = "Test content"
        category = "Random"
        tags = "Random,Test,API"

        post = Post.objects.create(
            title=title, 
            content=content,
            category=category, 
            tags=tags
        )
        
        post.save()
        return JsonResponse({"data": "created successfully"})
