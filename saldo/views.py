from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response
from datetime import datetime
from django.forms.models import modelformset_factory
from saldo.models import *
from saldo.forms import *

    #############
    #           #
    #   Index   #
    #           #
    #############

def index(request):
	prof_list = Professor.objects.all()
	encargo_list = Encargo.objects.all()
	ano = []
	sem = [1,2]
	for e in encargo_list:
		ano.append(int(e.ano))
	ano.sort(key=int)
	ano = set(ano)
	context = {'encargo_list':encargo_list,'ano':ano,'sem':sem}
	return render_to_response('saldo/index.html', context)

    #################
    #               #
    #   Professor   #
    #               #
    #################

def addprof(request):
    f = modelformset_factory(Professor,ProfessorForm)
    form = f(request.POST or None)
    if request.method == 'POST':
        f_nome = request.POST.get('nome')
        
        prof = Professor(nome = f_nome)
        prof.save()
        
        return redirect('/index/')
    context = {'form': form}
    return render(request,"saldo/addprof.html", context)

    ###############
    #             #
    #   Encargo   #
    #             #
    ###############

def addencargo(request):
    f = modelformset_factory(Encargo,EncargoForm)
    prof_list = Professor.objects.all()
    form = f(request.POST or None)
    if request.method == 'POST':
        f_professor = request.POST.get('professor')
        f_ano = request.POST.get('ano')
        f_sem = request.POST.get('sem')
        f_horas = request.POST.get('horas')
        f_encargos = request.POST.get('encargos')
        f_pontos =int(f_encargos) - int(f_horas)
        
        encargo = Encargo(professor_id = f_professor, ano = f_ano, sem = f_sem, horas = f_horas, encargos = f_encargos, pontos = f_pontos)
        encargo.save()
							
        return redirect('/calcularmedia/')
    context = {'form': form,'prof_list':prof_list}
    return render(request,"saldo/addencargo.html", context)


def calcularmedia(request):
	media_list = Media.objects.all()
	semestre_list = []
	professor_list = Professor.objects.all()
	encargo_list = Encargo.objects.all()
	pontos = 0
	med = 0
	asomar = 0
    
	for e in encargo_list:
		semestre_list.append(e.ano + "/" + e.sem)
		
	semestre_list = set(semestre_list)
    
	for i in semestre_list:
		numprof = 0
		pontos = 0
		for e in encargo_list:
			if i == e.ano + "/" + e.sem:
				pontos += e.pontos
				if e.horas > 0: numprof += 1
		med = pontos / numprof
		f = False
		for m in media_list:
			if m.anosem == i:
				m.nelementos = numprof
				m.somapt = pontos
				m.media = med
				m.save()
				f = True
		if f == False: Media(nelementos=numprof, somapt = pontos, media = med, anosem = i).save()
	
	for m in media_list:
		for e in encargo_list:
			anosem = e.ano + e.sem
			if anosem == m.anosem:
				asomar = e.pontos - m.media
				e.somar = asomar
				e.save() 
	return redirect('/saldo/')

def saldo(request):
	professor_list = Professor.objects.all()
	encargo_list = Encargo.objects.all()
	media_list = Media.objects.all()
	
	for e in encargo_list:
		for m in media_list:
			anosem = e.ano + "/" + e.sem
			if m.anosem in anosem:
				e.somar = e.pontos - m.media
				e.save()
	
	for e in encargo_list:
		for i in encargo_list:
			if e.professor.id == i.professor.id:
				ai = int(e.ano)
				si = int(e.sem)
				af = int(i.ano)
				sf = int(i.sem)
				if af == ai+1 and sf == 1:
					i.saldo_i = e.saldo_f
				else :
					if af == ai and si == 1 and sf == 2:
						i.saldo_i = e.saldo_f			
				i.save()
	
	for e in encargo_list:
		e.saldo_f = e.somar + e.saldo_i
		e.save()
	
	return redirect('/index/')	
    
def versaldo(request, anosem):
	encargo_list = Encargo.objects.all()
	saldo_list = []
	
	for e in encargo_list:
		if anosem == (e.ano+""+e.sem):
			saldo_list.append(e)
	
	context = {'encargo_list':encargo_list, 'saldo_list':saldo_list}
	return render(request,"saldo/versaldo.html", context)