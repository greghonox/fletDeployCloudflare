from asyncio import run
from typing import Callable
from __init__ import *
from motor_jobs import Jobs


class BarSearch(UserControl):
    def __init__(self, composition_func: Callable):
        super().__init__()
        self.composition_func = composition_func
        self.run_work = False
        self.search_jobs = Jobs()

    async def add_work_in_table(self, e):
        cont_page = 1
        profession = e.control.value
        self.tab_clear()
        while not self.run_work:
            jobs = self.search_jobs.browser(profession, cont_page)
            cont_page += 1
            for job in jobs:
                self.composition_func(job[0], job[1], job[2], 
                                      job[3], job[4], job[5], job[6])
    
    def tab_clear(self) -> None:
        self.page.controls[1].controls[0].content.controls[0].\
            tabs[0].content.content.controls[0].controls = []
        
    def widgets(self) -> Column:
        content = Container(
        )
        content.content=Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                TextField(
                    focused_border_color='blue',
                    width=900,
                    suffix_icon=icons.SEARCH,                        
                    text_align='center',
                    border=border.all(10),
                    border_color='white',
                    border_radius=8,
                    hint_text='Digite a vaga desejada...',
                    helper_text='Campo de busca de vaga...',
                )                       
            ]
        )
        return content
        
    def build(self) -> Column:
        column = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.START
        )
        column.controls = [
            self.widgets()
        ]
        return column
    
    
