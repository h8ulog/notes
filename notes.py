import json

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
app=QApplication([])
'''Інтерфейс програми'''
# параметри вікна програми
notes_win=QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900,600)

list_notes=QListWidget()
list_notes_label=QLabel('Список заміток')

button_note_create=QPushButton('Створити замітку')
button_note_del=QPushButton('Видалити замітку')
button_note_save=QPushButton('Зберегти замітку')
field_tag=QLineEdit('')
field_tag.setPlaceholderText('Введіть тег...')
field_text=QTextEdit()
button_tag_add=QPushButton('Додати до замітки')
button_tag_del=QPushButton('Відкріпити від замітки')
button_tag_search=QPushButton('Шукати замітки по тегу')
list_tags=QListWidget()
list_tags_label=QLabel('Список тегів')

layout_notes=QHBoxLayout()
col_1=QVBoxLayout()
col_1.addWidget(field_text)

col_2=QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1=QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2=QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_text)
row_3=QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_note_del)
row_4=QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_1,stretch=1)
notes_win.setLayout(layout_notes)




def save_note():
    if list_notes.selectedItems()[0].text()
        key=list_notes.selectedItems()[0].text()
        notes[key]['текст']=field_text.toPlainText()
        with open('notes_data.json','r') as file:
            json.dump(notes,file,sort_keys=True)
        with open('notes_data.json','r') as file:
            notes=json.load(file)
        list_notes.addItems(notes)
    else:
        print("Замітка для збереження не вибрана!")
button_note_save.clicked.connect(save )
def del_note():
    if list_notes.selectedItems()
        key=list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        with open('notes_data.json','w') as file:
            json.dump(notes,file,sort_keys=True)
    else:
        print("Замітка для видалення не вибрана!")
button_note_del.clicked.connect(del_note)











notes_win.show()
app.exec_()