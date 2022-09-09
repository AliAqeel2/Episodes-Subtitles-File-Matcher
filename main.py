import os
from tkinter import *
from tkinter import filedialog

gui_win = Tk()
gui_win.title('Episode-Subtitle Matcher')
gui_win.geometry('400x300')
gui_win.grid_rowconfigure(0, weight=1)
gui_win.grid_columnconfigure(0, weight=1)

label = StringVar()
errorLabel = StringVar()


def directory():
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


dialog_btn = Button(gui_win, text='select a folder', command=directory, width=15, height=2)
dialog_btn.pack(pady=20)

label_path = Label(gui_win, textvariable=label, font='italic 8', wraplength=350, justify=CENTER)
label_path.pack(pady=20)

error_label = Label(gui_win, textvariable=errorLabel, font='italic 8')
error_label.pack(pady=20)

gui_win.mainloop()
