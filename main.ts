let running = false
let end = 0
let start = 0
let false_start = false
input.onPinPressed(TouchPin.P0, function () {
    fidget()
})
function stop () {
    if (running) {
        running = false
        end = input.runningTime()
        basic.showLeds(`
            # # . . .
            # # . . .
            # # . . .
            # # . . .
            # # . . .
            `)
        basic.pause(1000)
        basic.showNumber(end - start)
    } else {
        false_start = true
        basic.showLeds(`
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            `)
    }
}
input.onButtonPressed(Button.A, function () {
    basic.showNumber(0)
})
function alarm () {
    radio.sendString("Good Morning!")
    basic.pause(1800000)
    radio.sendString("Eat and Drink")
    basic.pause(5400000)
    radio.sendString("Drink")
    basic.pause(5400000)
    radio.sendString("Drink")
    basic.pause(5400000)
    radio.sendString("Eat and Drink")
    basic.pause(5400000)
    radio.sendString("Drink")
    basic.pause(9000000)
    radio.sendString("Eat and Drink")
    basic.pause(9000000)
    radio.sendString("Drink")
    basic.pause(9000000)
    radio.sendString("Drink")
    basic.pause(10800000)
    radio.sendString("Sleep")
}
// def on_button_pressed_a():
// basic.show_number(gatorParticle.heartbeat(HeartbeatType.BPM))
// input.on_button_pressed(Button.A, on_button_pressed_a)
// Alarm
input.onPinPressed(TouchPin.P2, function () {
    alarm()
})
// Breathing
function breathing () {
    for (let index = 0; index < 7; index++) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.pause(500)
        basic.showIcon(IconNames.SmallDiamond)
        basic.pause(500)
        basic.showIcon(IconNames.Diamond)
        basic.pause(2000)
        basic.showIcon(IconNames.SmallDiamond)
        basic.pause(500)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.pause(2000)
    }
    basic.clearScreen()
}
input.onButtonPressed(Button.AB, function () {
    running = false
    false_start = false
    end = 0
    start = 0
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    breathing()
})
// Fidget
input.onPinPressed(TouchPin.P1, function () {
    stop()
})
function fidget () {
    basic.showNumber(3)
    basic.showNumber(2)
    basic.showNumber(1)
    basic.clearScreen()
    running = false
    false_start = false
    basic.pause(1000 + randint(0, 2000))
    if (!(false_start)) {
        start = input.runningTime()
        running = true
        led.stopAnimation()
        basic.clearScreen()
        led.plot(randint(0, 4), randint(0, 4))
    }
}
