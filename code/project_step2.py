# Підключення необхідних бібліотек
import cv2

# Визначення джерел для відеоданих: файл або камера
sources = {'video': 'video.mp4', 'camera': 0}
# Відповідності між назвами колірних просторів та константами OpenCV для їх зміни.
colorspaces = {'Gray': cv2.COLOR_BGR2GRAY}

# Функція для зміни колірного простору
def colorspace_change(input_frame, colorspace):
    return cv2.cvtColor(input_frame, colorspace)

def main():
    # Відкриття відеофайлу
    cap = cv2.VideoCapture(sources.get('video'))
    
    # Перевірка готовності відеофайлу
    while cap.isOpened():
        # Зчитування кадрів
        ret, frame = cap.read()
        # При виникненні помилки зчитування
        if not ret:
            print("Помилка зчитування кадру з відеофайлу!")
            break

        # Зміна колірного простору зображення (фрейму)
        frame_gray = colorspace_change(frame, colorspaces['Gray'])

        # Відображення результату
        cv2.imshow('frame Grayscale', frame_gray)
        
        # Очікування натискання клавіші 'q' для виходу
        if cv2.waitKey(25) == ord('q'):
            break
            
    # Закриття відеофайлу
    cap.release()
    # Закриття всіх вікон OpenCV
    cv2.destroyAllWindows()

# Виклик головної функції при запуску програми
if __name__ == '__main__':
    main()
