import pyaudio
from vosk import Model, KaldiRecognizer
from scipy import signal
import numpy as np

# Настройка аудио записи
FORMAT = pyaudio.paInt16  # Формат аудиоданных (16 бит, стерео)
CHANNELS = 1  # Количество каналов (моно)
RATE = 16000  # Частота дискретизации (16 кГц)
CHUNK = 1024  # Количество фреймов в буфере

# Инициализация объектов для записи звука и распознавания речи
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
model = Model('models/ru')
rec = KaldiRecognizer(model, RATE)

# Настройка фильтрации шума
CUTOFF = 6000 # Частота среза (6 кГц)
FILTER_ORDER = 5 # Порядок фильтрации

b, a = signal.butter(FILTER_ORDER, CUTOFF, fs=RATE)

print("Listening...")

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)

        # Применение фильтрации шума
        filtered_data = signal.lfilter(b, a, np.frombuffer(data, dtype=np.int16)).astype(np.int16)
        filtered_bytes = filtered_data.tobytes()

        # Распознавание речи
        if rec.AcceptWaveform(filtered_bytes) and len(data) > 0:
            result = rec.Result()
            print(result)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Завершение записи и освобождение ресурсов
    stream.stop_stream()
    stream.close()
    p.terminate()
