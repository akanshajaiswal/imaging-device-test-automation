import serial


class SerialDevice:

    def __init__(self, port, baudrate=115200, timeout=2):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None

    def connect(self):
        self.connection = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=self.timeout
        )

    def disconnect(self):
        if self.connection and self.connection.is_open:
            self.connection.close()

    def send_command(self, command):
        if not self.connection or not self.connection.is_open:
            raise RuntimeError("Device is not connected")

        self.connection.write((command + "\n").encode())

        response = self.connection.readline().decode().strip()

        return response