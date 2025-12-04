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
LIST_02 = [
    "Practice animating body mechanics\n[Body mechanics will never disappear, so let's do some practice!]", 
    "Do a simple rig\n[Rigging is hard, so some practice will make it second nature!]",
    "Do a beat/storyboard to dialogue\n[This helps by getting your creative juices flowing!]",
    "Practice on python\n[Coding is a skill that can always be built upon! Let’s make some simple programs!]",
    "Do a technique breakdown\n[This shows people your way of thinking! Let’s break it down!]"
]
DEFAULT_LIST = ["Sketch for 5 minutes", "Pick a detail to refine", "Sign it or scrap it — both are wins!"]

'''DEFINE mapping called ART_LISTS that links specific (Q1-3) combinations to
their respective list'''
ART_LISTS = {
    ("A1", "B1", "C1"): LIST_01,
    ("A2", "B2", "C1"): LIST_01,
    ("A1", "B2", "C3"): LIST_01,
    ("A2", "B1", "C2"): LIST_02,
    ("A2", "B2", "C2"): LIST_02,
    ("A2", "B1", "C3"): LIST_02,
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
        "C1": "Social Media",
        "C2": "LinkedIn",
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

        # Radio Frame helper
        def create_radio_frame(title, var, options):
            frame = tk.LabelFrame(
                self, text=title, padx=10, pady=10,
                bg=FRAME_COLOR, fg=TEXT_COLOR,
                highlightbackground=ACCENT_COLOR
            )
            frame.pack(fill="x", padx=15, pady=5)
            for text, value in options:
                tk.Radiobutton(
                    frame, text=text, variable=var, value=value,
                    bg=FRAME_COLOR, fg=TEXT_COLOR, selectcolor=ACCENT_COLOR,
                    activebackground=ACCENT_COLOR
                ).pack(anchor="w")
        '''
DISPLAY Q1 using radio buttons:
    A1 → Let's get our hands dirty
    A2 → I want to sit down today
    A3 → I'm lazy'''

        create_radio_frame("Q1 – What's the vibe?", self.q1_var, [
            ("Let's get our hands dirty!", "A1"),
            ("I want to sit down today", "A2"),
            ("I'm lazy", "A3")
        ])
        '''
DISPLAY Q2 using radio buttons:
    B1 → I want to better my portfolio
    B2 → I want to work on refining my skills
    B3 → I'm lazy
'''
        create_radio_frame("Q2 – Why do you want to do these activities?", self.q2_var, [
            ("I want to better my portfolio!", "B1"),
            ("I want to work on refining my skills!", "B2"),
            ("I'm lazy", "B3")
        ])
        '''
DISPLAY Q3 using radio buttons:
    C1 → TikTok
    C2 → Instagram
    C3 → Nowhere, because I'm lazy
'''
        create_radio_frame("Q3 – Lastly, where should you post your work?", self.q3_var, [
            ("TikTok", "C1"),
            ("Instagram", "C2"),
            ("Nowhere, because I'm lazy", "C3")
        ])

        '''
DISPLAY button: "Get My List"
    WHEN CLICKED → RUN on_generate()
'''
        # Generate Button
        tk.Button(
            self, text="Get My List", command=self.on_generate,
            bg=ACCENT_COLOR, fg="white", activebackground="#D09CFF"
        ).pack(pady=10)

    def on_generate(self):
        name = self.name_var.get().strip() or "Artist"
        ans1, ans2, ans3 = self.q1_var.get(), self.q2_var.get(), self.q3_var.get()

        if not (ans1 and ans2 and ans3):
            messagebox.showwarning("Incomplete", "Please answer all three questions.")
            return

        art_list = get_art_list(ans1, ans2, ans3)
        '''
FUNCTION on_generate():
    READ name input OR default to "Artist"
    READ selected Q1, Q2, Q3 codes

    IF any question is unanswered:
        SHOW warning popup to tell user to answer
        STOP on close

    CALL get_art_list() to retrieve correct activity list
    FORMAT summary text using explain_q1/q2/q3 results
    '''
        popup = tk.Toplevel(self)
        popup.title("Your Tailored List")
        popup.configure(bg=FRAME_COLOR)
        popup.geometry("600x500")

        header_text = (
            f"Hi {name}!\n\n"
            "Your selections:\n"
            f"  - Vibe: {explain_q1(ans1)}\n"
            f"  - Reason: {explain_q2(ans2)}\n"
            f"  - Posting plan: {explain_q3(ans3)}\n\n"
            "Here’s your tailored activity list:\n"
        )

        header_label = tk.Label(
            popup, text=header_text,
            bg=FRAME_COLOR, fg=TEXT_COLOR,
            font=("Helvetica", 12), justify="left"
        )
        header_label.pack(pady=10, padx=10, anchor="w")

        text_box = tk.Text(
            popup, wrap="word", bg="#F2E6FF", fg="black",
            highlightbackground=ACCENT_COLOR, height=15
        )
        text_box.pack(fill="both", expand=True, padx=10, pady=5)

        for i, item in enumerate(art_list, start=1):
            text_box.insert(tk.END, f"{i}. {item}\n")

        
        tk.Button(
            popup, text="Close", command=popup.destroy,
            bg=ACCENT_COLOR, fg="white"
        ).pack(pady=10)
'''
    CREATE POPUP WINDOW
        SET background/theme
        SHOW:
            greeting
            explanation of selected choices
            formatted list of activities
        ADD "Close" button to exit popup

END FUNCTION
'''
'''
RUN main loop
PROGRAM ENDS
''' 
if __name__ == "__main__":
    app = DailyArtApp()
    app.mainloop()