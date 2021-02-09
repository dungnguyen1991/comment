from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Comment, Reply
from .forms import CommentForm

class CommentView(CreateView):
    form_class = CommentForm
    template_name = 'core/comment_form.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.all()
        context["comment_list"] = []
        for obj in comments:
            context["comment_list"].append({
                'comment': obj,
                'replys': Reply.objects.filter(comment=obj),
            })
        return context

class ReplyView(View):
    def post(self, request, *args, **kwargs):
        comment_id = request.POST.get("comment", 1)
        qs = Comment.objects.filter(id = comment_id)
        comment = qs.first()
        if request.user.is_authenticated:
            r = Reply(user = request.user, comment = comment, content= request.POST.get("content"))
            r.save()
        return redirect("comment-page")
