from django.shortcuts import render, redirect
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from django.shortcuts import render


# contient la logique du code
# Récupère les données nécessaires, prépare un contexte, et renvoie un template pour l'affichage
def upload_file(request):
    try: 
        if request.method == 'POST':
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                return render(request, 'upload.html', {'error': 'Le fichier doit être au format CSV.'})
            #render kat3yelt lle fichier html
            
            # Lecture du fichier CSV avec pandas
            data = pd.read_csv(csv_file)
            request.session['data'] = data.to_dict()  # Stocker les données en session
            
            return redirect('overview')  # Rediriger vers l'aperçu des données
        return render(request, 'upload.html')
    except Exception as e:
        return render(request, 'upload.html', {'error': 'An error has occured'})

def home(request):
    return render(request, 'home.html')

def overview(request):
    data = pd.DataFrame(request.session.get('data'))
    columns = data.columns.tolist()
    preview = data.head().to_html()  # Aperçu des premières lignes
    return render(request, 'overview.html', {'columns': columns, 'preview': preview})
    #katprocesser page html b jinja2

def statistics(request):
    data = pd.DataFrame(request.session.get('data'))
    column = request.GET.get('column')
    if column not in data.columns:
        return render(request, 'statistics.html', {'error': '', 'columns': data.columns})
    stats = data[column].describe().to_dict()  # Calcul des statistiques
    return render(request, 'statistics.html', {'stats': stats, 'columns': data.columns})


def visualize(request):
    data = pd.DataFrame(request.session.get('data'))  # recupere data frm session
    column = request.GET.get('column')  # Obtenir la colonne selected
    if column not in data.columns:
        return render(request, 'visualize.html', { 'columns': data.columns})

    # generate histogram 
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    histogram_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    #encode b base64 prcq les donnees sont ss frme de bits 
    # decode utf8 pour l'envoyer text

    buf.close()

    numeric_data = data.select_dtypes(include=['number'])
#select_dtypes on la donnr type d ecolonne 
    heatmap_base64 = None
    if not numeric_data.empty:
        # Ensure the numeric data doesn't include strings like dates
        try:
            plt.figure(figsize=(10, 6))
            sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
            buf = BytesIO()
            plt.savefig(buf, format='png')
            # BytesIO saves image's bits
            plt.close()
            buf.seek(0)
            heatmap_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            buf.close()
        except Exception as e:
            print(f"Error generating heatmap: {e}")
            heatmap_base64 = None

    # Renvoyer le rendu du template
    return render(request, 'visualize.html', {
     'image':  histogram_base64,
     'columns': data.columns,
     'heatmap': heatmap_base64,
     })

