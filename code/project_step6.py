import cv2
import numpy as np

# Визначення джерел для відеоданих: файл або камера
video_sources = {'video': 'video.mp4', 'camera': 0}
# Відповідності між назвами колірних просторів та константами OpenCV для їх зміни.
colorspaces = {'Gray': cv2.COLOR_BGR2GRAY}

class VideoVision:
    @staticmethod
    def process_frame(frame, process_func, *args, **kwargs):
        """
        Обробка кадру за допомогою вказаної функції.

        Args:
            frame: Вхідний кадр.
            process_func: Функція обробки кадру.
            *args: Позиційні аргументи для функції обробки.
            **kwargs: Ключові аргументи для функції обробки.

        Returns:
            Оброблений кадр.
        """
        return process_func(frame, *args, **kwargs)
    

    @staticmethod
    def capture_video(source):
        """
        Генератор для зчитування відео з вказаного джерела.

        Args:
            source: Джерело відеоданих.

        Yields:
            Кадри відео.
        """
        cap = cv2.VideoCapture(source)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Помилка зчитування кадру!")
                break
            yield frame
            if cv2.waitKey(25) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    @staticmethod
    def convert_to_GRAY(input_frame):
        """
        Конвертує зображення у відтінки сірого.

        Args:
            input_frame: Вхідне зображення.

        Returns:
            Зображення у відтінки сірого.
        """
        return cv2.cvtColor(input_frame, colorspaces.get('Gray'))

    @staticmethod
    def rotate_video(video, angle):
        """
        Повертає відео на заданий кут.

        Args:
            video: Відео, яке слід повернути.
            angle: Кут повороту в градусах.

        Returns:
            Повернуте відео.
        """
        num_rows, num_cols = video.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), angle, 1)
        rotated_video = cv2.warpAffine(video, rotation_matrix, (num_cols, num_rows))
        return rotated_video

    @staticmethod
    def detect_corners(image, max_corners=5, quality_level=0.01, min_dist=20):
        """
        Виявлення кутів на зображенні за допомогою алгоритму Ші-Томасі.

        Args:
            image: Зображення.
            max_corners: Максимальна кількість кутів, які слід знайти.
            quality_level: Мінімальне значення якості кута між 0 і 1.
            min_dist: Мінімальна відстань між знайденими кутами.

        Returns:
            Зображення з відзначеними кутами.
        """
        new_image = image.copy()
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(gray_image, max_corners, quality_level, min_dist)
        corners = np.float32(corners)
        for item in corners:
            x, y = item[0]
            cv2.circle(new_image, (int(x), int(y)), 5, 255, -1)
        return new_image

    @staticmethod
    def apply_motion_blur(image, kernel_size=3):
        """
        Застосовує фільтр з ефектом руху до зображення.

        Args:
            image: Зображення.
            kernel_size: Розмір ядра фільтра.

        Returns:
            Зображення з ефектом руху.
        """
        kernel_motion_blur = np.zeros((kernel_size, kernel_size))
        kernel_motion_blur[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
        kernel_motion_blur = kernel_motion_blur / kernel_size
        return cv2.filter2D(image, -1, kernel_motion_blur)

    @classmethod
    def display_menu(cls):
        """
        Меню для вибору опцій роботи з відео.

        Викликається користувачем для вибору опції з обробки відео.
        """
        while True:
            print("\nВиберіть опцію:")
            print("1. Захоплення відео")
            print("2. Захоплення вебкамери")
            print("3. Перетворення в відтінки сірого")
            print("4. Поворот відео")
            print("5. Виявлення кутів за методом Ші-Томасі")
            print("6. Фільтр з ефектом зсуву")
            print("7. Вихід")
            choice = input("Введіть свій вибір (1-7): ")

            if choice == '1':
                for frame in cls.capture_video(video_sources.get('video')):
                    cv2.imshow('frame', frame)
            elif choice == '2':
                for frame in cls.capture_video(video_sources.get('camera')):
                    cv2.imshow('frame', frame)
            elif choice == '3':
                cls.process_video(video_sources.get('video'), cls.convert_to_GRAY)
            elif choice == '4':
                angle = float(input("Введіть кут: "))
                cls.process_video(video_sources.get('video'), cls.rotate_video, angle=angle)
            elif choice == '5':
                max_corners = int(input("Введіть максимальну кільксть кутів: "))
                quality_level = float(input("Введіть рівень якості: "))
                min_distance = float(input("Введіть мінімальну відстань: "))
                cls.process_video(video_sources.get('video'), cls.detect_corners, max_corners=max_corners, quality_level=quality_level, min_dist=min_distance)
            elif choice == '6':
                kernel_size = int(input("Введіть розмір ядра: "))
                cls.process_video(video_sources.get('video'), cls.apply_motion_blur, kernel_size=kernel_size)
            elif choice == '7':
                break
            cv2.destroyAllWindows()

    @classmethod
    def process_video(cls, source, process_func, *args, **kwargs):
        """
        Обробка відео вказаною функцією.

        Args:
            source: Джерело відеоданих.
            process_func: Функція обробки відео.
            *args: Позиційні аргументи для функції обробки відео.
            **kwargs: Ключові аргументи для функції обробки відео.
        """
        cap = cv2.VideoCapture(source)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Помилка зчитування кадру з відеофайлу!")
                break
            processed_frame = cls.process_frame(frame, process_func, *args, **kwargs)
            cv2.imshow('processed_frame', processed_frame)
            if cv2.waitKey(25) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)

if __name__ == "__main__":
    VideoVision.display_menu()
