#if this script is executed directly, run the read_distance function in a loop
if __name__ == '__main__':
    print("starting distance measurement! Press ctrl+c to stop this script")
    time.sleep(1)

    while True:
        #track the current time so we can loop at regular intervals 
        loop_start_time = time.time()

        #Read the distance and output result
        distance = read_distance()
        if distance:
            print("Distance: %.1f cm" % (distance))
            if distance <= 10:
                espeak.synth("obstacle is nearby")

        #find out how much time to wait until we should loop again so that each loop lasts 1sec
        time_to_wait = loop_start_time + 1 -time.time()
        if time_to_wait > 0 :
            time.sleep(time_to_wait)