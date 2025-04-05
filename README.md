# YouTube Downloader con yt-dlp + ffmpeg

Este proyecto es una herramienta en Python que permite descargar videos de YouTube en la mejor calidad disponible (video + audio) usando `yt-dlp` y `ffmpeg`.

## ¿Qué hace?

- Descarga videos de YouTube en MP4
- Une automáticamente el video y el audio
- Usa un User-Agent aleatorio para evitar bloqueos
- Permite elegir la carpeta de destino

## Requisitos

- Python 3.10 o superior
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/)

## ¿Cómo usarlo?

1. Clona este repositorio o descargá los archivos.
2. Asegurate de tener `yt-dlp` y `ffmpeg` instalados y en tu PATH.
3. Ejecutá el script con:

```bash
python youtube-downloader.py
