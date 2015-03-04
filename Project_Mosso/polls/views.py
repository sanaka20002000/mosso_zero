# coding: UTF-8
from django.http import HttpResponseRedirect, HttpResponse,
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Poll, Choice

#
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.order_by('-pub_date')[:5]

#
#
class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

#
#
class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

#
#  
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
    # Redisplay the poll vdoting form.
        return render(request, 'polls/detail.html', {
             'poll': p,
             'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(p.id,)))
    
def book_list(request):
    books = Book.objects.all().order_by('id')
    return render_to_response('polls/book_list.html',  # 使用するテンプレート
         {'books': books},       # テンプレートに渡すデータ
         context_instance=RequestContext(request))  # その他標準のコンテキスト

def book_edit(request, book_id=None):
    '''書籍の編集'''
    return HttpResponse(u'書籍の編集')

def book_del(request, book_id):
    '''書籍の削除'''
    return HttpResponse(u'書籍の削除')