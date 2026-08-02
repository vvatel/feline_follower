# Feline Follower (Autonomous Pet-Tracking Robot)
<strong>WORK IN PROGRESS</strong>
<p>An autonomous mobile robot that utilizes real-time visual tracking and SLAM-based navigation to follow the fast, erratic motions of a Felis catus in a real, unmapped and obstacle-ridden environment. Specifically, this robot will be tracking my own cat</p>
<details><summary>Calypso</summary>
  <img width="300" height="400" alt="calypso" src="https://github.com/user-attachments/assets/761e2816-2d1a-450f-8220-0bf891518a11" />
</details>

## Progress Timeline

  <details> <summary><strong>7/31/26</strong> - Verified TB6612 (Motor Driver) control logic on breadboard</summary><br>
    <p>Bought a <a href=https://a.co/d/0d0911Pa>TB6612 Motor Driver</a> and soldered the header pins onto it. I tested the wiring between the Arduino, the motor driver, and one of the car's motors using a breadboard. Then, I wrote a <a href="arduino/tests/motor_driver_test/motor_driver_test.ino">script</a> (shown below) to test the motor driver's control logic.<br><br><b>Issue:</b>  After wiring in battery power, STBY unexpectedly read 0V. STBY needs to constantly be set to HIGH otherwise the motor driver operates in sleep mode. Isolated the fault via systematic voltage tracing using a multimeter and found a cold solder joint on the STBY header pin. Reheating the joint solved the issue.</p>
    
  https://github.com/user-attachments/assets/8c097552-bbd2-4168-9c4e-e303f9cf0ce9  
  </details>
  
  <details> <summary><strong>7/26/26</strong> - Redesigned robot control architecture</summary><br>
    <p>
      Initially thought to establish communication with a host computer running ROS2 to the onboard Arduino using a ESP32-S3 microcontroller (included with the kit) as the intermediary. Found that the I/O Expansion shield (placed on top of the Arduino) and the ESP32 were too customized/undocumented to extend for this         project. Decided to scrap both parts, and instead use a different microcontroller as the intermediary.<br><br><b>Notably:</b> Because of this replacement, I lost access to the motor driver (TB6612FNG) attached to the I/O Expansion Shield so I would need to wire in one on my own.<br><br>For the intermiedary, I           chose to use the Raspberry Pi Model 3 B+</b> (pictured below). This Pi was chosen mainly due to budget constraints. Since the project will initially run most computations through my desktop, the Pi only needs enough power to broadcast images over WI-FI, run ROS2 to receive commands, and translate those commands         into workable Serial that can be written to the motors. Though a stronger Pi could run the computations itself, it is too expensive at the moment. The final structure will look like:<br><br>Host Computer <---ROS2 Messages---> RPI 3B+ <----Serial----> Arduino
    </p>
    <img width=200 height=200 alt="Raspberry Pi 3B+" src="https://github.com/user-attachments/assets/7fdf3846-9356-4677-be20-b20eb48023ae" />

  </details>
  
  <details> <summary><strong>7/1/26</strong> - Built smart car from kit</summary><br>
    <p>Initially decided to purchase a cheap autonomous vehicle kit (pictured below). This would've allowed me to focus on writing the software for the project and not have to worry about custom-built hardware.</p>
    <img width=200 height=200 alt="Elegoo Smart Car" src="https://github.com/user-attachments/assets/0bfb81bb-cc9d-4f42-a743-23ac3eee5569" />

    
  </details>
  
  
  

