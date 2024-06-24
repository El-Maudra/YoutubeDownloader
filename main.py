from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.progressbar import MDProgressBar
from kivy.lang import Builder
from pytube import YouTube
import os
from android.permissions import request_permissions, Permission, check_permission
from android.storage import primary_external_storage_path
from kivy.clock import Clock
from threading import Thread

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
      # Defining the APK theme color
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        
        self.dialog = None
        self.progress_bar = MDProgressBar(value=0, max=100)
        
        # Request necessary permissions
        request_permissions([Permission.INTERNET, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
                
        return Builder.load_string(user_input)

    def download_url(self):
        url_input = self.root.ids.url_input.text
        if not check_permission(Permission.WRITE_EXTERNAL_STORAGE) or not check_permission(Permission.READ_EXTERNAL_STORAGE):
            self.show_error_dialog("Storage permissions are not granted.")
            return
        self.show_progress_dialog()
        Thread(target=self.download_youtube_video, args=(url_input,)).start()

    def show_progress_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Downloading",
                size_hint=(0.5, 1),
                type="custom",
                content_cls=self.progress_bar,
            )
        self.progress_bar.value = 0
        self.dialog.open()

    def show_error_dialog(self, message):
        error_dialog = MDDialog(
            title="Error",
            text=message,
            size_hint=(0.8, 1),
            buttons=[
                MDRectangleFlatButton(
                    text="Close", on_release=lambda x: error_dialog.dismiss()
                )
            ],
        )
        error_dialog.open()

    def update_progress_bar(self, percentage):
        self.progress_bar.value = percentage

    def download_youtube_video(self, video_url):
        def progress_callback(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            downloaded_size = total_size - bytes_remaining
            percentage = (downloaded_size / total_size) * 100
            Clock.schedule_once(lambda dt: self.update_progress_bar(percentage), 0)

        try:
            # Get the primary external storage path for saving the video
            save_path = os.path.join(primary_external_storage_path(), 'Download')
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            
            yt = YouTube(video_url, on_progress_callback=progress_callback)
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(save_path)
            self.dialog.dismiss()
            self.show_success_dialog(f"Downloaded '{yt.title}' successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.dialog.dismiss()
            self.show_error_dialog(f"An error occurred: {e}")

    def show_success_dialog(self, message):
        success_dialog = MDDialog(
            title="Success",
            text=message,
            size_hint=(0.8, 1),
            buttons=[
                MDRectangleFlatButton(
                    text="Close", on_release=lambda x: success_dialog.dismiss()
                )
            ],
        )
        success_dialog.open()

DownloaderVideo().run()
