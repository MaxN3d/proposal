'''PROGRM START

DEFINE colors for graphic user interface (GUI) theme

DEFINE activity lists (1-9)
DEFINE default_list for combinations/invalid choices

DEFINE mapping called ART_LISTS that links specific (Q1-3) combinations to
their respective list

-----------------------------------------------------------------
FUNCTION get_art_list(q1,q2,q3):
	IF (q1, q2, q3) exists in ART_LISTS:
        	RETURN the matching list
    	ELSE:
        	RETURN DEFAULT_LIST
END FUNCTION

FUNCTION explain_q1(code):
    RETURN vibe for question 1 selection
FUNCTION explain_q2(code):
    RETURN reason for question 2 selection
FUNCTION explain_q3(code):
    RETURN posting plan for question 3 selection
-----------------------------------------------------------------

CREATE main window pop-up
    SET title = "Daily Art List"
    SET window size and background color

CREATE name input field so it feels personal

DISPLAY Q1 using radio buttons:
    A1 → Let's get our hands dirty
    A2 → I want to sit down today
    A3 → I'm lazy

DISPLAY Q2 using radio buttons:
    B1 → I want to better my portfolio
    B2 → I want to work on refining my skills
    B3 → I'm lazy

DISPLAY Q3 using radio buttons:
    C1 → TikTok
    C2 → Instagram
    C3 → Nowhere, because I'm lazy

DISPLAY button: "Get My List"
    WHEN CLICKED → RUN on_generate()
-----------------------------------
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

RUN main loop
PROGRAM ENDS
''' 