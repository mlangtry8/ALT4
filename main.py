running = False
end = 0
start = 0
false_start = False

def on_pin_pressed_p0():
    fidget()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def stop():
    global running, end, false_start
    if running:
        running = False
        end = input.running_time()
        basic.show_leds("""
            # # . . .
            # # . . .
            # # . . .
            # # . . .
            # # . . .
            """)
        basic.pause(1000)
        basic.show_number(end - start)
    else:
        false_start = True
        basic.show_leds("""
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            """)
def alarm():
    radio.send_string("Good Morning!")
    basic.pause(1800000)
    radio.send_string("Eat and Drink")
    basic.pause(5400000)
    radio.send_string("Drink")
    basic.pause(5400000)
    radio.send_string("Drink")
    basic.pause(5400000)
    radio.send_string("Eat and Drink")
    basic.pause(5400000)
    radio.send_string("Drink")
    basic.pause(9000000)
    radio.send_string("Eat and Drink")
    basic.pause(9000000)
    radio.send_string("Drink")
    basic.pause(9000000)
    radio.send_string("Drink")
    basic.pause(10800000)
    radio.send_string("Sleep")
# def on_button_pressed_a():
    # basic.show_number(gatorParticle.heartbeat(HeartbeatType.BPM))
# input.on_button_pressed(Button.A, on_button_pressed_a)
# Alarm

def on_pin_pressed_p2():
    alarm()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

# Breathing
def breathing():
    for index in range(7):
        basic.pause(2000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        basic.pause(500)
        basic.show_leds("""
            . . . . .
            . . # . .
            . # . # .
            . . # . .
            . . . . .
            """)
        basic.pause(500)
        basic.show_leds("""
            . . # . .
            . # . # .
            # . . . #
            . # . # .
            . . # . .
            """)
        basic.pause(2000)
        basic.show_leds("""
            . . . . .
            . . # . .
            . # . # .
            . . # . .
            . . . . .
            """)
        basic.pause(500)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    basic.clear_screen()

def on_button_pressed_ab():
    global running, false_start, end, start
    running = False
    false_start = False
    end = 0
    start = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    breathing()
input.on_button_pressed(Button.B, on_button_pressed_b)

# Fidget

def on_pin_pressed_p1():
    stop()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def fidget():
    global running, false_start, start
    basic.show_number(3)
    basic.show_number(2)
    basic.show_number(1)
    basic.clear_screen()
    running = False
    false_start = False
    basic.pause(1000 + randint(0, 2000))
    if not (false_start):
        start = input.running_time()
        running = True
        led.stop_animation()
        basic.clear_screen()
        led.plot(randint(0, 4), randint(0, 4))
