import urllib.request
import tkinter as tk
import subprocess
import winreg
import ctypes
import sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# ---------------------------------------------------------⬇download_DisableTelemetry⬇---------------------------------------------------------- #

def download_file(url, local_path):
    try:
        username = os.environ['USERNAME']
        local_path = local_path.replace('%USERNAME%', username)

        # Adicione esta linha para imprimir o caminho final
        print(f'Caminho final do arquivo: {local_path}')

        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        urllib.request.urlretrieve(url, local_path)

        print(f"Download concluído: {local_path}")

        return True

    except Exception as e:
        print(f"Erro durante o download: {e}")
        return False
    
def on_painel_start():
    # URL do arquivo
    url = 'https://raw.githubusercontent.com/SanGraphic/QuickBoost/main/v2/DisableTelemetry.bat'

    # Caminho local para salvar o arquivo
    local_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Frosty Boost', 'DisableTelemetry.bat')

    # Chamada da função para baixar o arquivo
    if download_file(url, local_path):
        # Mensagem de confirmação
        print("Arquivo baixado com sucesso. O processo será executado agora...")
        subprocess.run(local_path, shell=True)
    else:
        print("Falha ao baixar o arquivo.")

# ---------------------------------------------------------⬆download_DisableTelemetry⬆---------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------⬇disable_mouse_acceleration⬇--------------------------------------------------------- #

def disable_mouse_acceleration():
    key_path = r'Control Panel\Mouse'

    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, 'MouseSpeed', 0, winreg.REG_SZ, '0')
        winreg.SetValueEx(registry_key, 'MouseThreshold1', 0, winreg.REG_SZ, '0')
        winreg.SetValueEx(registry_key, 'MouseThreshold2', 0, winreg.REG_SZ, '0') 
    except Exception as e:
        print(f"Erro ao desativar a aceleração do mouse: {e}")
    finally:
        winreg.CloseKey(registry_key)

# ---------------------------------------------------------⬆disable_mouse_acceleration⬆--------------------------------------------------------- #
        
# ---------------------------------------------------------⬇a⬇--------------------------------------------------------- #


def disable_startup_telemetry():
    print("Lower Input latency & Improved responsiveness")

def lower_input_latency():
    print("Lower Input latency & Improved responsiveness")

def disable_unnecessary_system_services():
    print("Disable Unnecessary System Services")

def remove_preinstalled_apps():
    print("Remove Pre-installed Apps")

def lower_system_usage():
    print("Lower system usage & Unwanted Bloatware")

def disable_powersaving():
    print("Disable Powersaving")

def import_quickboost_powerplan():
    print("Import QuickBoost PowerPlan")

def apply_system_profile_tweaks():
    print("Apply System Profile Tweaks")

#-----------------------------------------------------------⬇disable_startup_programs⬇-----------------------------------------------------------#

def disable_startup_programs():
    subprocess.run(['explorer', 'ms-settings:startupapps'])

#-----------------------------------------------------------⬆disable_startup_programs⬆-----------------------------------------------------------#

def apply_all_tweaks():
    print("Apply All Tweaks")

painel = tk.Tk()
painel.title("Frosty boost")
painel.resizable(False, False)
painel.configure(bg="black")

frame = tk.Frame(painel)
frame.pack(padx=10, pady=10)
frame.configure(bg="black")

tk.Button(frame, text="Disable Startup Telemetry (ok)", command=disable_startup_telemetry).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Disable Mouse Acceleration (ok)", command=disable_mouse_acceleration).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame, text="Lower Input latency & Improved responsiveness", command=lower_input_latency).grid(row=2, column=1, padx=5, pady=5)
tk.Button(frame, text="Disable Unnecessary System Services", command=disable_unnecessary_system_services).grid(row=3, column=0, padx=5, pady=5)
tk.Button(frame, text="Remove Pre-installed Apps", command=remove_preinstalled_apps).grid(row=3, column=1, padx=5, pady=5)
tk.Button(frame, text="Lower system usage & Unwanted Bloatware", command=lower_system_usage).grid(row=4, column=0, padx=5, pady=5)
tk.Button(frame, text="Disable Powersaving", command=disable_powersaving).grid(row=4, column=1, padx=5, pady=5)
tk.Button(frame, text="Import QuickBoost PowerPlan", command=import_quickboost_powerplan).grid(row=5, column=0, padx=5, pady=5)
tk.Button(frame, text="Apply System Profile Tweaks", command=apply_system_profile_tweaks).grid(row=5, column=1, padx=5, pady=5)
tk.Button(frame, text="Disable Start-up Programs (Manual)(ok)", command=disable_startup_programs).grid(row=6, column=1, padx=5, pady=5)
tk.Button(frame, text="Apply All Tweaks", command=apply_all_tweaks).grid(row=7, column=0, columnspan=2, padx=5, pady=5)

painel.mainloop()




def download_file(url, local_path):
    try:

        username = os.getlogin()

        local_path = local_path.replace('%USERNAME%', username)

        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        urllib.request.urlretrieve(url, local_path)

        print(f"Download concluído: {local_path}")

        return True

    except Exception as e:
        print(f"Erro durante o download: {e}")
        return False

def on_painel_start():

    url = 'https://raw.githubusercontent.com/SanGraphic/QuickBoost/main/v2/DisableTelemetry.bat'

    local_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Frosty Bosst', 'DisableTelemetry.bat')

    if download_file(url, local_path):
        print("Arquivo baixado com sucesso. Executando agora...")
        subprocess.run(local_path, shell=True)
    else:
        print("Falha ao baixar o arquivo.")