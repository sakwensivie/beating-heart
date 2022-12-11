basic.show_leds("""
    . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
""")
basic.pause(2000)
music.play_melody("A F A G F E G F ", 500)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(100)
    basic.show_icon(IconNames.SMALL_HEART)
    basic.pause(100)
basic.forever(on_forever)
