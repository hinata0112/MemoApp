from django.shortcuts import render
from django.views import generic
from .models import Memo
from django.urls import reverse_lazy
from itertools import groupby

class ListMemoView(generic.ListView):
    template_name = 'memo/memo_list.html'
    model = Memo
    context_object_name = 'Memo'

class DetailMemoView(generic.DetailView):
    template_name = 'memo/memo_detail.html'
    model = Memo
    context_object_name = 'Memo'

class CreateMemoView(generic.CreateView):
    template_name = 'memo/memo_create.html'    
    model = Memo
    context_object_name = 'Memo'
    fields = ('title', 'content', 'tag')
    success_url = reverse_lazy('memo-list')

class DeleteMemoView(generic.DeleteView):
    template_name = 'memo/memo_delete.html'
    model = Memo
    context_object_name = 'Memo'
    success_url = reverse_lazy('memo-list') 

class UpdateMemoView(generic.UpdateView):
    template_name = 'memo/memo_update.html' 
    model = Memo
    context_object_name = 'Memo'
    fields = ('title', 'content', 'tag')
    success_url = reverse_lazy('memo-list')
