# Підключення необхідних бібліотек
import cv2

# Визначення джерел для відеоданих: файл або камера
sources = {'video': 'video.mp4', 'camera': 0}

def main():
    # Зчитування даних з відеофайлу
    cap_video = cv2.VideoCapture(sources.get('video'))
    
    # Перевірка готовності відеофайлу
    while cap_video.isOpened():
        # Зчитування кадрів
        ret, frame = cap_video.read()
        # При виникненні помилки зчитування
        if not ret:
            print("Помилка зчитування кадру з відеофайлу!")
            break
        # Відображення кадру
        cv2.imshow('frame', frame)
        # Очікування натискання клавіші 'q' для виходу
        if cv2.waitKey(25) == ord('q'):
            break
    # Закриття відеофайлу
    cap_video.release()
    
    # Зчитування даних з відеокамери
    cap_web = cv2.VideoCapture(sources.get('camera'))
    # Перевірка готовності веб-камери
    while cap_web.isOpened():
        # Зчитування кадрів
        ret, frame = cap_web.read()
        # При виникненні помилки зчитування
        if not ret:
            print("Помилка зчитування кадру з веб-камери!")
            break
        # Відображення кадру
        cv2.imshow('frame', frame)
        # Очікування натискання клавіші 'q' для виходу
        if cv2.waitKey(25) == ord('q'):
            break
    # Закриття відеокамери
    cap_web.release()
    
    # Закриття всіх вікон OpenCV
    cv2.destroyAllWindows()

# Виклик головної функції при запуску програми
if __name__ == '__main__':
    main()
