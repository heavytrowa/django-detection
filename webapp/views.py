from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os
# def index1(request):
#     return HttpResponse(os.system('''python scripts/fetch.py'''))
# need to make this function work
def index(request):
    #return HttpResponse("<h2>HEY!<h2>")
    # return HttpResponse(os.system(''' python fetch.py'''))
    return HttpResponse(os.system('''python scripts/fetch.py && python2 -m scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=0.jpg
        '''))
      #return HttpResponse(subprocess.Popen(["python","tf_files/test1.py"],close_fds=True))
