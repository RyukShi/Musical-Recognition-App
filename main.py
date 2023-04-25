import os
from music import Music


def main():
    AUDIO_DIRECTORY_PATH = os.path.join(os.getcwd(), 'audio')
    audio_files = [os.path.join(AUDIO_DIRECTORY_PATH, f) for f in os.listdir(
        AUDIO_DIRECTORY_PATH) if f.endswith(".mp3")]

    analyzed_music = []
    for audio_file_path in audio_files:
        music = Music(audio_file_path)
        music.plot_spectrum()
        analyzed_music.append(music)


if __name__ == '__main__':
    main()
