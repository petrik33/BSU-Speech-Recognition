from vosk import Model, KaldiRecognizer
import wave

model = Model("models/ru")  # Загрузка модели для русского языка
rec = KaldiRecognizer(model, 16000)

# Открытие аудиофайла
wf = wave.open("filtered_audio.wav", "rb")

# Чтение всех данных из аудиофайла
data = wf.readframes(wf.getnframes())

# Обработка данных через Vosk
rec.AcceptWaveform(data)

# Получение результата
result = rec.FinalResult()

# Вывод распознанного текста
print(result)
