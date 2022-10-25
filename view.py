import PySimpleGUI as sg

def main():
    end_btn = [sg.Button("X", size=(10, 5))]
    inny = [sg.Button("go", size=(10, 5))]
    backgroud = [sg.Image('images/carbon.jpeg', size=(800, 480))]
    label = [sg.Text('Hello', background_color=("red"))]
    layout = [label, end_btn, inny, backgroud]

    #create the window
    window = sg.Window("Demo", layout, size=(800, 480))

    #event loop
    while True:
        event, values = window.read()
        # if close window or press ok button
        if  event == sg.WIN_CLOSED or event == 'X':
            break
        if event == 'go':
            print("elo")

    window.close()

if __name__ == '__main__':
    main()
