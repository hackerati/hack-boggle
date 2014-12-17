from django.shortcuts import render
from django.http import HttpResponse
from utils import GameBoard, WordDictionary
import json

def index(request):

    gb = GameBoard()
    c = {
        'game_board': gb
    }

    return render(request, 'index.html', c)


def new_board(request):
    # TODO: If client requests new board,
    # return new board and render client-side.
    gb = GameBoard()

    return HttpResponse(json.dumps(gb.board))


def is_valid_word(request):
    # TODO: should return to the client
    # true if the word is valid, else false.
    # Render response on client side.

    return 'true'
