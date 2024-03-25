import PySimpleGUI as sg
sg.theme("LightGreen")

def veids(jaut):
    if jaut in radio_jaut:
        return [
            [sg.Text(jaut)],
            [sg.Radio(text, "choice", key=f'radio_{text}') for text in radio_jaut[jaut]],
            [sg.Button("Next")]
        ]
    else:
        return [
            [sg.Text(jaut)],
            [sg.InputText(key='atbildes')],
            [sg.Button("Next")]
        ]


jautajums = [
    "1. Jautājums: Kuri bija pirmie cilvēki, kas pieradināja kaķus",
    "2. Jautājums: Kas lielākajai daļai cilvēku patīk labāk: suņi vai kaķi?",
    "3. Jautājums: Kurš ir vienīgais zīdītājs, kas spēj lidot?", 
    "4. Jautājums: Jā vai nē: jūras zvaigznēm ir smadzenes.", 
    "5. Jautājums: Cik muskuļu vienā kaķa ausī?",
    "6. Jautājums: Kurā gadā pirmais kaķis tika sūtīts kosmosā? (Rakstiet tikai skaitli - punktu nevajag)", 
    "7. Jautājums: Kuri ir vienīgie putni, kas spēj lidot atpakaļgaitā?"
    "8. Jautājums: Cik % no pasaules svin savu suņu dzimšanas dienu?" 
]


atbildes = [
    "Ēģiptieši",
    "Suņi",
    "Sikspārnis",
    "Nē",
    "32",
    "1963", 
    "Kolibri",
    "9%",
]

radio_jaut = {
    "2. Jautājums: Kas lielākajai daļai cilvēku patīk labāk: suņi vai kaķi?": ["Suņi", "Kaķi"],
    "4. Jautājums: Jā vai nē: jūras zvaigznēm ir smadzenes.": ["Jā", "Nē"],
    "5. Jautājums: Cik muskuļu vienā kaķa ausī?": ["4", "12", "32", "37"],
    "7. Jautājums: Kuri ir vienīgie putni, kas spēj lidot atpakaļgaitā?": ["Kolibri", "Pūces", "Pīles", "Ērgļi"],
    "8. Jautājums: Cik % no pasaules svin savu suņu dzimšanas dienu?": ["3%", "15%", "9%", "30%"]
}

tagadejais_jaut = 0
rez = 0




window = sg.Window("Viktorīna", veids(jautajums[tagadejais_jaut]))


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Next":

        if jautajums[tagadejais_jaut] in radio_jaut:
            pareiza = atbildes[tagadejais_jaut].lower()
            user_answer = next((a.split('_')[1] for a, b in values.items() if a.startswith('radio') and b), '').lower()
            if user_answer == pareiza:
                rez += 1
        else:
            if values['atbildes'].strip().lower() == atbildes[tagadejais_jaut].lower():
                rez += 1
        

        tagadejais_jaut += 1
        if tagadejais_jaut < len(jautajums):
            window.close()
            window = sg.Window("Viktorīna", veids(jautajums[tagadejais_jaut]))
        else:
            sg.popup(f"Rezultāts: {rez}/{len(jautajums)}")
            break


window.close()