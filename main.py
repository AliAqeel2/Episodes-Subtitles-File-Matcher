import os
from tkinter import *
from tkinter import filedialog
import zipfile
from send2trash import send2trash

gui_win = Tk()
gui_win.title('Episode-Subtitle Matcher')
gui_win.geometry('400x300')
gui_win.grid_rowconfigure(0, weight=1)
gui_win.grid_columnconfigure(0, weight=1)

label = StringVar()
errorLabel = StringVar()


def unzip():
    path = filedialog.askopenfilename(title="Select The Zip Folder")
    if path == '':
        return
    parentPath = os.path.abspath(os.path.join(path, os.pardir))
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(parentPath)


def deleteSubtitles():
    path = filedialog.askdirectory(title="Select The Folder")
    if path == '':
        return
    entries = os.listdir(path)
    for entry in entries:
        if entry.endswith('.srt') or entry.endswith('.ass'):
            temp = path + '\\' + entry
            path_to_delete = temp.replace("/", "\\")
            send2trash(path_to_delete)


def mainFunction():
    path = filedialog.askdirectory(title="Select The Folder")
    if path == '':
        return
    label.set(path)
    entries = os.listdir(path)

    videoTypes = ['.mkv', '.mp4']
    episodeType = ''
    episodesNames = []
    numberOfEpisodes = 0

    subtitleIndex = 0
    subtitleTypes = ['.srt', '.ass']
    subtitleType = ''

    try:
        for entry in entries:
            if any(x in entry for x in videoTypes):
                numberOfEpisodes += 1
                episodesNames.append(entry)

        if episodesNames[0].endswith('.mkv'):
            episodeType = '.mkv'
        elif episodesNames[0].endswith('.mp4'):
            episodeType = '.mp4'

        for entry in entries:
            if any(x in entry for x in subtitleTypes):
                if entry.endswith('.srt'):
                    subtitleType = '.srt'
                elif entry.endswith('.ass'):
                    subtitleType = '.ass'

        for entry in entries:
            if entry.endswith(subtitleType):
                subtitleFilePath = path + '\\' + entry
                episodesNamesPath = path + '\\' + episodesNames[subtitleIndex]
                episodesNamesPath = episodesNamesPath.replace(episodeType, subtitleType)
                os.rename(subtitleFilePath, episodesNamesPath)
                subtitleIndex += 1
                if subtitleIndex > numberOfEpisodes:
                    break
        errorLabel.set('Successfully Renamed All Subtitles')
        error_label.config(fg='green')
    except:
        errorLabel.set('Sorry, Something went wrong')
        error_label.config(fg='red')


menu = Menu(gui_win)
gui_win.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label='Extra', menu=fileMenu)
fileMenu.add_command(label='Unzip a file', command=unzip)
fileMenu.add_command(label='Delete all subtitles', command=deleteSubtitles)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=gui_win.quit)

dialog_btn = Button(gui_win, text='select a folder', command=mainFunction, width=15, height=2)
dialog_btn.pack(pady=20)

label_path = Label(gui_win, textvariable=label, font='italic 8', wraplength=350, justify=CENTER)
label_path.pack(pady=20)

error_label = Label(gui_win, textvariable=errorLabel, font='italic 8')
error_label.pack(pady=20)

gui_win.mainloop()
