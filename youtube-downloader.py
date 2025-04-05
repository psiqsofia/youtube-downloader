import subprocess
import random

USER_AGENTS = [
    # Tu lista de user agents
]

def limpiar_cache():
    try:
        subprocess.run(["C:/Users/jsofi/programasao/yt-dlp/yt-dlp.exe", "--rm-cache-dir"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

def descargar_video(url, output_path="."):
    try:
        user_agent = random.choice(USER_AGENTS)

        comando = [
            "yt-dlp",
            "-f", "bv*+ba/best",
            "--user-agent", user_agent,
            "--merge-output-format", "mp4",
            "-o", f"{output_path}/%(title)s.%(ext)s",
            url
        ]

        subprocess.run(comando, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("Error: No se pudo descargar el video. Intenta con otro enlace o configura cookies.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    limpiar_cache()
    url = input("Introduce la URL del video de YouTube: ")
    output_path = "C:/Users/jsofi/Downloads"
    descargar_video(url, output_path)

