from __init__ import *
from table import TableWidget


class BodyCenter(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.table = TableWidget(self.page)
        
    def build(self) -> Container:
        _width = 800
        _height = 350
        content = Container(
            width=self.page.window_width + _width,
            height=self.page.window_height + _height,              
        )
        content.content=Row(
            expand=True,
            controls=[
                Tabs(
                    width=self.page.window_width + _width,
                    height=self.page.window_height+ _height, 
                    scrollable=True,
                    selected_index=0,
                    animation_duration=300,
                     tabs=[
                         self.tab_jobs(),
                         self.tab_settings(),
                    ],
                )
            ]
        )
        return content
    
    def tab_jobs(self) -> Tab:
        tab = Tab(
            text='Vagas',
            icon=icons.SEARCH_ROUNDED,
            content=Container(
                border_radius=10,
                content=self.table
            )
        )

        return tab

    def tab_settings(self) -> Tab:
        tab = Tab(
            text='Configurações',
            icon=icons.SETTINGS_ACCESSIBILITY_ROUNDED,
        )
        return tab    