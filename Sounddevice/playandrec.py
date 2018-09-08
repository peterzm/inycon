import sounddevice as sd
import numpy as np
import pylab as plt
import time
from scipy.signal import find_peaks
from scipy import signal



def playrec_tone(frecuencia, duracion, amplitud=0.1, fs=192000):
    """
    Emite un tono y lo graba.
    """
    sd.default.samplerate = fs #frecuencia de muestreo
    sd.default.channels = 2,2 #por las dos salidas de audio
    
    cantidad_de_periodos = duracion*frecuencia
    puntos_por_periodo = int(fs/frecuencia)
    puntos_totales = puntos_por_periodo*cantidad_de_periodos
    
    tiempo, data = generador_de_senhal(frecuencia, duracion, amplitud, 'sin')      
    grabacion = sd.playrec(data, blocking=True)
    
    return tiempo, data, grabacion


