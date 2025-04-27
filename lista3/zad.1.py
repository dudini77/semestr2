import datetime
import os
import shutil
def backup(katalogi, rozszerzenie):
    """
    Tworzy kopię zapasową plików o określonych rozszerzeniach z podanych katalogów,
    które zostały zmodyfikowane w ciągu ostatnich 3 dni.

    Argumenty:
    katalogi (list): Lista ścieżek do katalogów, w których ma być szukane.
    rozszerzenie (list): Lista rozszerzeń plików (np. ['.png', '.jpg']), które mają być kopiowane.

    Zwraca:
    None
    (drukuje informację o każdym skopiowanym pliku)
    """
    x = datetime.date.today()
    backup_folder= os.path.join('nowy_backup', f"{x}")
    os.makedirs(backup_folder, exist_ok=True)
    y= datetime.datetime.now()
    z= x-datetime.timedelta(days=100)
    for katalog in katalogi:
        for root, dirs, files in os.walk(katalog):
            for file in files:
                if any(file.lower().endswith(ext.lower()) for ext in rozszerzenie):
                    file_path= os.path.join(root, file)
                    mytime= datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                    if mytime >= z:
                        relative= os.path.relpath(root, katalog)
                        backup_path= os.path.join(backup_folder, relative)
                        os.makedirs(backup_path, exist_ok=True)
                        shutil.copy2(file_path, backup_path)
                        print(f"Skopiowano: {file_path} -> {backup_path}")
backup(["semestr2"], [".png"])
                    