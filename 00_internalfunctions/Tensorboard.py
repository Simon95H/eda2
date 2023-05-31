import threading
from tensorboard import program


class TensorBoardThread(threading.Thread):
    def __init__(self, log_path, port=6006):
        super(TensorBoardThread, self).__init__()
        self.log_path = log_path
        self.port = port
        self.tb = program.TensorBoard()
        self.tb.configure(argv=[None, '--logdir', self.log_path, '--port', str(self.port)])
        self.url = None

    def run(self):
        self.url = self.tb.launch()
        print(f"TensorBoard listening on {self.url}")

    def stop(self):
        self.tb._exiting = True
        print("CLOSE")

    def __del__(self):
        self.stop()
        print("DESTROY")

