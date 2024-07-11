#First UI with PySimpleGUI Library

import PySimpleGUI as psg;
  
#All the stuff inside my window.
layout = [
            [psg.Text("What is your name?", key="name")],
            [psg.InputText()],
            [psg.Text("Where do you from?", key="locale")],
            [psg.InputText()],
            [psg.Text("How old are you?", key="age")],
            [psg.InputText()],
            [psg.Button("Insert", key="button"), psg.Button("Cancel")]
        ];

#Create the window
window = psg.Window("Simple Form", layout);

#Event loop to process the "events" and get the "values" of the inputs
while True:
    events, values = window.read();

    if events == psg.WIN_CLOSED or events == "Cancel":
        print("Bye!");
        break;
    
    print("Hello, ", values[0], "! Nice to me you!", values[1], "? WOW, it's so cool!");

window.close();
