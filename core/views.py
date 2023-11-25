from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.views import View
from .forms import ActivoForm, ReportForm
from .models import Activo, Report


def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:  # Si el usuario es administrador
            return redirect('admin_home')
        else:
            return redirect('user_home')
    else:
        return render(request, 'home.html')


@login_required
def products(request):
    return render(request, 'products.html')


@login_required
def user_home(request):
    return render(request, 'user_home.html')


@login_required
def admin_home(request):
    if request.user.is_staff:  # Solo permite el acceso a administradores
        return render(request, 'admin_home.html')
    else:
        # Redirige a usuarios normales a su página correspondiente
        return redirect('user_home')


def exit(request):
    logout(request)
    return redirect('home')


class CreateActivoView(View):
    template_name = 'core/create_activo.html'

    def get(self, request):
        form = ActivoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ActivoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Activo creado exitosamente.')
            return redirect('activos')
        else:
            messages.error(
                request, 'Hubo un error al crear el activo. Por favor, revisa el formulario.')
            return render(request, self.template_name, {'form': form})


class ActivosView(View):
    def get(self, request):
        activos = Activo.objects.all()
        return render(request, 'core/activos.html', {'activos': activos})


class CreateReportView(View):
    template_name = 'core/create_report.html'

    def get(self, request):
        form = ReportForm()

        activos = Activo.objects.all()

        selected_activo = 'YourActivotTitulo'

        return render(request, self.template_name, {'form': form, 'activos': activos, 'selected_activo': selected_activo})

    def post(self, request):
        form = ReportForm(request.POST)

        activos = Activo.objects.all()

        selected_activo = 'YourActivotTitulo'

        if form.is_valid():
            form.save()
            messages.success(request, 'Reporte creado exitosamente.')
            return redirect('reports')
        else:
            messages.error(
                request, 'Hubo un error al crear el reporte. Por favor, revisa el formulario.')
            return render(request, self.template_name, {'form': form, 'activos': activos, 'selected_activo': selected_activo})


class ReportsView(View):
    def get(self, request):
        reports = Report.objects.all()
        return render(request, 'core/Reports.html', {'reports': reports})


def eliminar_activo(request, activo_id):
    activo = get_object_or_404(Activo, pk=activo_id)
    activo.delete()
    return redirect('activos')


def eliminar_reporte(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    report.delete()
    return redirect('reports')
