import numpy as np
import plotly.express as px
from librosa import load, stft, amplitude_to_db


class Music:
    def __init__(
        self,
        audio_file_path: str,
        verbose: bool = True,
        auto_run: bool = True
    ):
        self.audio_file_path = audio_file_path
        self.verbose = verbose
        if auto_run:
            self.run_analysis()

    def run_analysis(self):
        self.load_audio()
        self.compute_spectrum()

    def load_audio(self):
        # load audio with librosa
        self.y, self.sr = load(self.audio_file_path)
        if self.verbose:
            print(
                f"Audio data: {self.y}\n Sample Rate: {self.sr}")

    def compute_spectrum(self):
        self.S = np.abs(stft(self.y))
        if self.verbose:
            print(self.S)

    def plot_spectrum(self):
        fig = px.imshow(
            amplitude_to_db(self.S, ref=np.max),
            labels=dict(x="Time", y="Frequency", color="Inferno")
        )
        fig.show()
