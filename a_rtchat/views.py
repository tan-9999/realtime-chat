from django.shortcuts import render, get_object_or_404,redirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .models import *
from .forms import ChatmessageCreateForm


# Create your views here.
@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name="public chats")
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()
    
    if request.method == 'POST':
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            return redirect('home')
    
    return render(request,'a_rtchat/chat.html',{'chat_messages': chat_messages, 'form': form})


