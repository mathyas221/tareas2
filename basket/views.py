from django.shortcuts import render, get_object_or_404
from basket.models import Player
from basket.forms import PlayerForm
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from basket.forms import *


def index(request):
    data = {}

    # SELECT * FROM player
    data['object_list'] = Player.objects.all().order_by('-id')

    template_name = 'player/list_player.html'
    return render(request, template_name, data)


def add(request):
    data = {}
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()

    template_name = 'player/add_player.html'
    return render(request, template_name, data)


def list(request):
    if request.method == 'POST':
        get_object_or_404(Player, pk=request.POST['id']).delete()
        return JsonResponse({})
    data = {'players': Player.objects.all()}
    template_name = "player/listar.html"
    return render(request, template_name, data)

def detail(request, player_id):

    data = {}
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()

    return render(request, template_name, data)

def edit(request, player_id):
    data={}
    if request.method == "POST":
        player = EditForm(request.POST, request.FILES, instance=Player.objects.get(pk=player_id))
        if player.is_valid():
            player.save()

    template_name = 'player/edit_player.html'
    data['persona'] = EditForm(instance=Player.objects.get(pk=player_id))
    return render(request, template_name, data) 

# def edit(request, player_id):
#     post = get_object_or_404(Post, pk=player_id)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post= form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('post_detail', pk=player_id)
#     else:
#         form = PostForm(instance=post)
#         return render(request, 'player/edit_player.html', {'form': form})
