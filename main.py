import os
from tkinter.filedialog import askdirectory

path = askdirectory()
entries = os.listdir(path)

videoTypes = ['.mkv', '.mp4']
subtitleIndex = 0
numberOfEpisodes = 0
episodeType = ''
episodesNames = []

for entry in entries:
    if any(x in entry for x in videoTypes):
        numberOfEpisodes += 1
        episodesNames.append(entry)

if episodesNames[0].endswith('.mkv'):
    episodeType = '.mkv'
elif episodesNames[0].endswith('.mp4'):
    episodeType = '.mp4'

for entry in entries:
    if entry.endswith('.srt'):
        subtitleFilePath = path + '\\' + entry
        episodesNamesPath = path + '\\' + episodesNames[subtitleIndex]
        episodesNamesPath = episodesNamesPath.replace(episodeType, '.srt')
        os.rename(subtitleFilePath, episodesNamesPath)
        subtitleIndex += 1
        if subtitleIndex > numberOfEpisodes:
            break
