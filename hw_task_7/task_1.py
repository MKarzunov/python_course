import cv2
import pathlib


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


class FaceDetector:
    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.prepare_data(self.path)

    def prepare_data(self, path: pathlib.Path):
        if path.suffix in ('.jpg', '.png', '.webp', '.bmp', '.gif'):
            self.image = cv2.imread(path.name)
        elif path.suffix in ('.mp4', '.avi', '.mov', '.wmv', '.webm'):
            self.video = cv2.VideoCapture(path.name)
        else:
            raise TypeError('Unknown file extension')

    @staticmethod
    def detection(frame):
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        found_faces = face_cascade.detectMultiScale(grayscale, 1.2, 6)
        return found_faces

    def inference(self):
        if hasattr(self, 'image'):
            found_faces = self.detection(self.image)
            for (x, y, w, h) in found_faces:
                center = (int(x + w / 2), int(y + h / 2))
                axes = (int(w / 2), int(h / 2))
                cv2.ellipse(self.image, center, axes, 0, 0, 360, (0, 0, 255), 4)
        else:
            self.video_result = []
            while True:
                ret, frame = self.video.read()
                if ret:
                    found_faces = self.detection(frame)
                    for (x, y, w, h) in found_faces:
                        center = (int(x + w / 2), int(y + h / 2))
                        axes = (int(w / 2), int(h / 2))
                        res_frame = cv2.ellipse(frame, center, axes, 0, 0, 360, (0, 0, 255), 4)
                        self.video_result.append(res_frame)
                else:
                    break
            self.video.release()

    def display(self, width=None, height=None):
        if hasattr(self, 'image'):
            if width or height:
                h, w = self.image.shape[:2]
                if width is None:
                    ratio = height / h
                    dimension = (int(w * ratio), height)
                else:
                    ratio = width / w
                    dimension = (width, int(h * ratio))
                self.image = cv2.resize(self.image, dimension)
            cv2.imshow('picture', self.image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            for frame in self.video_result:
                if frame is not None:
                    if width or height:
                        h, w = frame.shape[:2]
                        if width is None:
                            ratio = height / h
                            dimension = (int(w * ratio), height)
                        else:
                            ratio = width / w
                            dimension = (width, int(h * ratio))
                        frame = cv2.resize(frame, dimension)
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            self.video.release()
            cv2.destroyAllWindows()


face = FaceDetector('person.png')
face.inference()
face.display(700, None)
