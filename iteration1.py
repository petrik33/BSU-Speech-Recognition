import pyaudio
import wave

FORMAT = pyaudio.paInt16  # Формат аудиоданных (16 бит, стерео)
CHANNELS = 1  # Количество каналов (моно)
RATE = 16000  # Частота дискретизации (16 кГц)
CHUNK = 1024  # Количество фреймов в буфере

audio = pyaudio.PyAudio()

# Настройка для записи с микрофона
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Запись аудио в файл (для простоты примера записываем только 5 секунд)
for i in range(0, int(RATE / CHUNK * 5)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# Остановка потока записи и завершение работы с устройством
stream.stop_stream()
stream.close()
audio.terminate()

# Сохранение записанного аудио в файл wav
with wave.open("recorded_audio.wav", "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
