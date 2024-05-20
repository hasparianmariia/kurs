# Підключення необхідних бібліотек
import cv2
import numpy as np

# Визначення джерел для відеоданих: файл або камера
sources = {'video': 'video.mp4', 'camera': 0}

# Фільтрація з ефектом зсуву
def motion_blur(image, kernel_size=3):
    # Створення ядра фільтра руху
    kernel_motion_blur = np.zeros((kernel_size, kernel_size))
    kernel_motion_blur[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
    kernel_motion_blur = kernel_motion_blur / kernel_size
    # Застосування фільтра до зображення
    return cv2.filter2D(image, -1, kernel_motion_blur)

def main():
    # Відкриття відеофайлу
    cap = cv2.VideoCapture(sources.get('video'))
    
    # Перевірка готовності відеофайлу
    while cap.isOpened():
        # Зчитуємо кадри
        ret, frame = cap.read()
        # При виникненні помилки зчитування
        if not ret:
            print("Помилка зчитування кадру з відеофайлу!")
            break

        # Застосовуємо фільтр руху до кадру
        frame_changed = motion_blur(frame, kernel_size=7)

        # Відображення результату
        cv2.imshow('frame_changed', frame_changed)
        
        # Очікування натискання клавіші 'q' для виходу
        if cv2.waitKey(25) == ord('q'):
            break
            
    # Закриття відеофайлу
    cap.release()
    # Закриття всіх вікон OpenCV
    cv2.destroyAllWindows()

# Перевірка, чи це головний файл для запуску програми
if __name__ == '__main__':
    main()
