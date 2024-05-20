import cv2

# Визначення джерел для відеоданих: файл або камера
sources = {'video': 'video.mp4', 'camera': 0}

# Функція повороту відео на заданий кут
def rotate(video, angle):
    # Отримання розмірів відео
    num_rows, num_cols = video.shape[:2]
    # Створення матриці повороту
    rotation_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), angle, 1)
    # Поворот відео за допомогою матриці повороту
    img_rotation = cv2.warpAffine(video, rotation_matrix, (num_cols, num_rows))
    return img_rotation

def main():
    # Відкриття відеофайлу
    cap = cv2.VideoCapture(sources.get('video'))
    
    # Перевірка готовності відеофайлу
    while cap.isOpened():
        # Зчитування кадрів
        ret, frame = cap.read()
        # При виникненні помилки зчитування
        if not ret:
            print("Помилка зчитування кадру!")
            break

        # Поворот кадру на -32 градусів
        frame_rotate = rotate(frame, -32)

        # Відображення результату
        cv2.imshow('frame', frame_rotate)
        
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
