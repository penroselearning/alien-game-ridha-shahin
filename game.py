WIDTH = 900
HEIGHT = 900

LIVES = 5
alien_status = ""
score = 0
speed = 1
game_status = 0

alien = Actor('alien')
alien.pos = 10, 250

def draw():
    if game_status == 0:
        screen.blit("space1", (0, 0))
        screen.draw.text("Click enter to start the game", (80, 300), fontname="maldini", fontsize=70, color="white")
    if LIVES == 0:
        screen.draw.text("Aw! Game over, better luck next time", (100, 300), fontname="maldini", fontsize=90, color="white")

    if game_status == 1:
        screen.clear()
        screen.blit("space1", (0, 0))
        alien.draw()
        screen.draw.text(f"score:{str(score)}", (100, 10), fontname="zealot", fontsize=50, color="white")
        screen.draw.text(f'Remaining Lives : {str(LIVES)}', (WIDTH-400, 30), color="white", fontname="zealot", fontsize=24)
        screen.draw.text("TRY TO HIT ME", (300, 400), fontname="maldini", fontsize=60, color="white")


    if alien_status == "Hit":
        screen.draw.text("Ouch, Move your mouse", (100, 300), fontname="maldini", fontsize=30, color="white")
    elif alien_status == "Missed":
        screen.draw.text("Haha, You missed", (100, 300), fontname="maldini", fontsize=30, color="white")


    if LIVES == 0:
        screen.clear()
        screen.blit("gameover", (0, 0))
        screen.draw.text("Aw, better luck next time", (80, 300), fontname="maldini", color="white", fontsize=50)

def update():
    global speed, LIVES, score, alien_status, game_status
    if game_status == 0:
        if keyboard.RETURN:
            game_status =1

    if game_status ==1:
        alien.left +=speed
    if alien.left>WIDTH:
        alien.left = 15
    if LIVES <= 0:
        LIVES = 0
    if speed <=1:
        speed = 1
    if score <=0:
        score = 0
def on_mouse_down(pos):
    global speed, score, LIVES, alien_status, game_status

    if alien.collidepoint(pos):
        score +=1
        speed +=1
        alien_status = "Hit"
        alien.image = "alien_hurt"
        sounds.eep.play()
        clock.schedule_unique(set_alien_normal, 0.3)
    else:
        score -=1
        speed -=1
        LIVES -=1
        alien_status ="Missed"

def set_alien_normal():
    alien.image = 'alien'