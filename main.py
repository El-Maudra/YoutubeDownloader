from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.progressbar import MDProgressBar
from kivy.lang import Builder
from pytube import YouTube
import os

user_input = """
Screen:
    MDTextField:
        id: url_input
        hint_text: "Paste url here"
        helper_text: "paste youtube url video"
        helper_text_mode: "on_focus"
        icon_right: "download"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300

    MDRectangleFlatButton:
        text: "Download"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: app.download_url()
"""

class DownloaderVideo(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        
        self.dialog = None
        self.progress_bar = MDProgressBar(value=0, max=100)
        
        return Builder.load_string(user_input)

    def download_url(self):
        url_input = self.root.ids.url_input.text
        self.show_progress_dialog()
        self.download_youtube_video(url_input)

    def show_progress_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Downloading",
                size_hint=(0.5, 1),
                type="custom",
                content_cls=self.progress_bar,
            )
        self.dialog.open()

    def download_youtube_video(self, video_url):
        def progress_callback(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            downloaded_size = total_size - bytes_remaining
            percentage = (downloaded_size / total_size) * 100
            self.progress_bar.value = percentage

        try:
            save_path = '.'
            yt = YouTube(video_url, on_progress_callback=progress_callback)
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(save_path)
            self.dialog.dismiss()
            print(f"Downloaded '{yt.title}' successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.dialog.dismiss()

DownloaderVideo().run()
