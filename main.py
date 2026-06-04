import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.1, 1)

class MenuUtama(Screen):
    def __init__(self, **kwargs):
        super(MenuUtama, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        judul = Label(
            text="PETA BATIN\nEngine Resona v2", 
            font_size='28sp', 
            bold=True,
            halign='center',
            color=(0.2, 0.6, 1, 1)
        )
        layout.add_widget(judul)
        
        sub_judul = Label(
            text="Selamat datang di ruang kontemplasi digital.\nSilakan pilih menu di bawah untuk memulai.",
            font_size='14sp',
            halign='center',
            color=(0.8, 0.8, 0.8, 1)
        )
        layout.add_widget(sub_judul)
        
        btn_mulai = Button(
            text="Buka Peta",
            size_hint=(1, 0.2),
            background_color=(0.1, 0.5, 0.8, 1),
            font_size='18sp',
            bold=True
        )
        btn_mulai.bind(on_press=self.ke_halaman_peta)
        layout.add_widget(btn_mulai)
        
        self.add_widget(layout)

    def ke_halaman_peta(self, instance):
        self.manager.current = 'halaman_peta'

class HalamanPeta(Screen):
    def __init__(self, **kwargs):
        super(HalamanPeta, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        konten = Label(
            text="[ Peta Batin Sedang Terbuka ]\n\nBerjalan mulus di atas framework Kivy.\nNalareka Digital Assets © 2026",
            font_size='16sp',
            halign='center'
        )
        layout.add_widget(konten)
        
        btn_kembali = Button(
            text="Kembali ke Menu",
            size_hint=(1, 0.15),
            background_color=(0.7, 0.2, 0.2, 1),
            font_size='16sp'
        )
        btn_kembali.bind(on_press=self.ke_menu_utama)
        layout.add_widget(btn_kembali)
        
        self.add_widget(layout)

    def ke_menu_utama(self, instance):
        self.manager.current = 'menu_utama'

class PetaBatinApp(App):
    def build(self):
        self.title = "Peta Batin"
        sm = ScreenManager()
        sm.add_widget(MenuUtama(name='menu_utama'))
        sm.add_widget(HalamanPeta(name='halaman_peta'))
        return sm

if __name__ == '__main__':
    PetaBatinApp().run()
