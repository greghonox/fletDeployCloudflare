from __init__ import *
from random import randint


class TableWidget(UserControl):
    def __init__(self, page: Page) -> None:
        super().__init__()
        self.page = page
        self.table = Column(
            expand=True,
            scroll='auto',
            width=self.page.window_width + 900,
            height=self.page.window_height + 1500,
        )
        
    def set_text(self, text: str, width: int=300) -> Text:
        return Text(
            text,
            expand=True,
            color='white',
            width= width,
            text_align='left',
            selectable=True
        )

    def add_data_table(self, job: str, salary: str, beneficy: str,
            description: str, requirements: str, contact: str, url: str) -> None:
        self.table.controls.append(
            Container(
                bgcolor='yellow900',
                width=self.page.window_width + 1000,
                height=100,
                border_radius=25,
                padding=padding.only(bottom=5, top=5),
                margin=0,
                content=Row(
                    
                    controls=[                        
                        self.set_text(job, 5),
                        self.set_text(salary, 2),
                        self.set_text(beneficy),
                        self.set_text(description),
                        self.set_text(requirements),
                        self.set_text(contact, 10),
                        self.set_text(url),
                        
                    ]            
                )
            )
        )
        self.table.update()

    def build(self) -> DataTable:
        return self.table
