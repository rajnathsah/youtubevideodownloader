from tkinter import *
from tkinter.ttk import *
from pytube import YouTube


class DownloadWindow(Frame):
    '''
    DownloadWindow form
    '''
    def __init__(self, master=None):
        '''
        Initialize frame
        '''
        Frame.__init__(self, master)        
        self.grid()        

        self.master.title('Download')

        self.videoAudio = ['--Select--', 'Video', 'Audio']

        self.outputQuality = ['--Select--', 'High', 'Low']               

        self.empyLine = Label(master, text="")
        self.empyLine.grid(row=1, column=0)        

        self.videoLabel = Label(master, text="YouTube URL")
        self.videoLabel.grid(row=2, column=0)
        
        self.videoUrl = StringVar()
        self.videoEntry = Entry(master, textvariable=self.videoUrl)
        self.videoEntry.grid(row=2, column=1)

        self.typeLabel = Label(master, text="Type(Video/Audio)")
        self.typeLabel.grid(row=3, column=0)
        
        self.typeOutput = Combobox(master, state="readonly", values=self.videoAudio, width=17)
        self.typeOutput.grid(row=3, column=1)
        self.typeOutput.current(0)

        self.qualityLabel = Label(master, text="Quality")
        self.qualityLabel.grid(row=4, column=0)

        self.typeQuality = Combobox(master, state="readonly", values=self.outputQuality, width=17)
        self.typeQuality.grid(row=4, column=1)
        self.typeQuality.current(0)                                            

        self.button = Button(master, text = "Download", command=self.downloadContent)
        self.button.grid(row = 5, column = 1)  


    def downloadContent(self):
        try:            
            youtube_video_url = self.videoUrl.get()
 
            yt_obj = YouTube(youtube_video_url)

            if self.typeOutput.get() == 'Video' and self.typeQuality.get() == 'High':
                yt_obj.streams.filter(type='video').get_highest_resolution().download()
            elif self.typeOutput.get() == 'Video' and self.typeQuality.get() == 'Low':
                yt_obj.streams.filter(type='video').get_lowest_resolution().download()
            elif self.typeOutput.get() == 'Audio':            
                yt_obj.streams.get_audio_only().download()

        except Exception as ex:
            print(ex)
        finally:
            self.master.destroy()


if __name__ == '__main__':
    downloadRoot = Tk()    
    downloadRoot.resizable(0,0)
    downloadRoot.eval('tk::PlaceWindow . center')
    DownloadWindow(downloadRoot)
    downloadRoot.mainloop()
