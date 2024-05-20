import cv2
import numpy as np

# Визначення джерел для відеоданих: файл або камера
sources = {'video': 'video.mp4', 'camera': 0}

# Функція для детектування кутів за допомогою алгоритму Ші-Томасі
def corner_detector(image, max_corners=5, quality_level=0.01, min_dist=20):
    # Копіюємо вхідне зображення
    new_image = image.copy()
    # Перетворюємо зображення в відтінки сірого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Знаходимо кути за допомогою алгоритму Ші-Томасі
    corners = cv2.goodFeaturesToTrack(gray_image, max_corners, quality_level, min_dist)
    corners = np.float32(corners)
    # Відображаємо знайдені кути на зображенні
    for item in corners:
        x, y = item[0]
        cv2.circle(new_image, (int(x), int(y)), 5, 255, -1)
    return new_image

def main():
    # Відкриваємо відеофайл
    cap = cv2.VideoCapture(sources.get('video'))
    
    # Перевірка готовності відеофайлу
    while cap.isOpened():
        # Зчитуємо кадри
        ret, frame = cap.read()
        # При виникненні помилки зчитування
        if not ret:
            print("Помилка зчитування кадру з відеофайлу!")
            break

        # Викликаємо функцію детектування кутів
        frame_changed = corner_detector(frame, 10, 0.001, 35)

        # Відображаємо результат
        cv2.imshow('frame_changed', frame_changed)
        
        # Очікуємо натискання клавіші 'q' для виходу
        if cv2.waitKey(25) == ord('q'):
            break
            
    # Закриваємо відеофайл
    cap.release()
    # Закриваємо всі вікна OpenCV
    cv2.destroyAllWindows()

# Перевіряємо, чи це головний файл для запуску програми
if __name__ == '__main__':
    main()
