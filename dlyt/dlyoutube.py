import pytube
import PySimpleGUI as sg

safeToDl = False
sg.theme("DarkGrey")

layout = [[sg.Text("What video would you like to convert? ")],[sg.Input(key = "-IN-")],[sg.Text(size=(40,1), key='-OUTPUT-')],[sg.Button("Confirm",key = "Status"),sg.Button("Quit")],[sg.Text("Download Location:",key = "Textloc")],[sg.Input(key = "in2",change_submits=True),sg.FolderBrowse(key = 'folder')]]

window = sg.Window("Download Youtube",layout)

def dl(url,loc = "C:/Users/caelu/Downloads"):

	try:
		if url=="":
			return "Please enter a url"
		else:
			pytube.YouTube(str(url)).streams.get_highest_resolution().download(loc)
	except Exception:
		return "Not a valid url "
	else:
		return "Done, want to download another?"

while True:
	loc = ""
	event,values = window.Read()
	if event == sg.WINDOW_CLOSED or event == "Quit":
		break
	elif safeToDl:
		vidstatus = dl(values['-IN-'],values['in2'])
		window['-OUTPUT-'].update(vidstatus)
		window['Status'].update("Confirm")
		safeToDl = False
	elif event == "Status" and not safeToDl:
		window['-OUTPUT-'].update("Hold on don't pannic")
		window['Status'].update("Download")
		window['Textloc'].update("Location: "+values['folder'])
		safeToDl = True
		

window.close()

if __name__ == '__dlyoutube__':
	dlyoutube()
