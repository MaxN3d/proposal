'''PROGRM START'''
import tkinter as tk
from tkinter import messagebox

'''DEFINE colors for graphic user interface (GUI) theme'''
BG_COLOR = "#D7BFDC"
FRAME_COLOR = "#9966CB"
ACCENT_COLOR = "#B200ED"
TEXT_COLOR = "#ffffff"

'''DEFINE activity lists (1-9)'''
LIST_01 = [
    "Do some figure drawing\n[Studying the human form will help with perspective and dynamic poses!]",
    "Pottery\n[Getting your hands dirty always helps break up a mundane routine!]",
    "Character designs\n[This gets your creative juices flowing!]",
    "Artist Study\n[Who's someone you idolize? Do a study on their work!]",
    "Painting\n[Painting always helps refine color theory, form, and composition — plus it's fun!]"
]

'''DEFINE default_list for combinations/invalid choices'''
LIST_02 = ["Activity A", "Activity B", "Activity C"]
DEFAULT_LIST = ["Sketch for 5 minutes", "Pick a detail to refine", "Sign it or scrap it — both are wins!"]

'''DEFINE mapping called ART_LISTS that links specific (Q1-3) combinations to
their respective list'''
ART_LISTS = {
    ("A1", "B1", "C1"): LIST_01,
    ("A2", "B2", "C1"): LIST_01,
    ("A1", "B2", "C3"): LIST_01,
    # Add more combos later...
}


'''
FUNCTION get_art_list(q1,q2,q3):
	IF (q1, q2, q3) exists in ART_LISTS:
        	RETURN the matching list
    	ELSE:
        	RETURN DEFAULT_LIST
END FUNCTION'''
def get_art_list(ans1, ans2, ans3):
    return ART_LISTS.get((ans1, ans2, ans3), DEFAULT_LIST)
'''
FUNCTION explain_q1(code):
    RETURN vibe for question 1 selection
FUNCTION explain_q2(code):
    RETURN reason for question 2 selection
FUNCTION explain_q3(code):
    RETURN posting plan for question 3 selection
'''
def explain_q1(ans1):
    return {
        "A1": "Let's get our hands dirty!",
        "A2": "I want to sit down today.",
        "A3": "I'm lazy."
    }.get(ans1, "Unknown vibe.")

def explain_q2(ans2):
    return {
        "B1": "I want to better my portfolio!",
        "B2": "I want to work on refining my skills!",
        "B3": "I'm lazy."
    }.get(ans2, "Unknown motivation.")

def explain_q3(ans3):
    return {
        "C1": "TikTok",
        "C2": "Instagram",
        "C3": "Nowhere, because I'm lazy."
    }.get(ans3, "Unknown posting place.")
'''
CREATE main window pop-up
    SET title = "Daily Art List"
    SET window size and background color'''
class DailyArtApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Daily Art List")
        self.geometry("700x650")
        self.configure(bg=BG_COLOR)

        # Store answers
        self.name_var = tk.StringVar()
        self.q1_var = tk.StringVar()
        self.q2_var = tk.StringVar()
        self.q3_var = tk.StringVar()

        self.create_widgets()
    
    def create_widgets(self):
        # Title
        tk.Label(
            self, text="Daily Art List",
            font=("Comic Sans MS", 24, "bold"),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=10)
        '''
CREATE name input field so it feels personal'''
        # Name Input
        name_frame = tk.Frame(self, bg=BG_COLOR)
        name_frame.pack(pady=5)
        tk.Label(
            name_frame, text="Your name:",
            bg=BG_COLOR, fg=TEXT_COLOR
        ).pack(side=tk.LEFT)
        tk.Entry(
            name_frame, textvariable=self.name_var,
            width=25, bg="white", fg="black",
            highlightbackground=ACCENT_COLOR
        ).pack(side=tk.LEFT, padx=5)
'''
DISPLAY Q1 using radio buttons:
    A1 → Let's get our hands dirty
    A2 → I want to sit down today
    A3 → I'm lazy'''

'''
DISPLAY Q2 using radio buttons:
    B1 → I want to better my portfolio
    B2 → I want to work on refining my skills
    B3 → I'm lazy
'''
'''
DISPLAY Q3 using radio buttons:
    C1 → TikTok
    C2 → Instagram
    C3 → Nowhere, because I'm lazy
'''
'''
DISPLAY button: "Get My List"
    WHEN CLICKED → RUN on_generate()
'''
'''
FUNCTION on_generate():
    READ name input OR default to "Artist"
    READ selected Q1, Q2, Q3 codes

    IF any question is unanswered:
        SHOW warning popup to tell user to answer
        STOP on close

    CALL get_art_list() to retrieve correct activity list
    FORMAT summary text using explain_q1/q2/q3 results

    CREATE POPUP WINDOW
        SET background/theme
        SHOW:
            greeting
            explanation of selected choices
            formatted list of activities
        ADD "Close" button to exit popup

END FUNCTION
-----------------------------------
'''
'''
RUN main loop
PROGRAM ENDS
''' 