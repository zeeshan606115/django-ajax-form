from django.shortcuts import render
from .models import Info
from .forms import InfoModelForm
from django.http import JsonResponse
# Create your views here.
def info_add_view(request):
	form = InfoModelForm(request.POST or None)
	data ={}

	if request.method == 'POST':
		print('works')
		name = request.POST.get('name')
		description = request.POST.get('description')
		Info.objects.create(name=name, description=description)
		data['name'] = name
		data['description'] = description
		return  JsonResponse(data, safe=False)
	context = {
		'form': form
	}

	return render(request, 'infos/main.html', context)
