# Feline Follower (Autonomous Pet-Tracking Robot)
<strong>WORK IN PROGRESS</strong>
<p>An autonomous mobile robot that utilizes real-time visual tracking and SLAM-based navigation to follow the fast, erratic motions of a Felis catus in a real, unmapped and obstacle-ridden environment. Specifically, this robot will be tracking my own cat, Calypso, around my room and the hallways of the floor where I live.</p>
<p align="center"><img width="300" height="400" alt="calypso" src="https://github.com/user-attachments/assets/761e2816-2d1a-450f-8220-0bf891518a11" /></p>


## Details
<details><summary><ins><strong>Architecture</strong></ins></summary>
  
```
Desktop (ROS2/SLAM) <--Wi-Fi/ROS2--> Raspberry Pi 3B+ <--UART--> Arduino Uno R3 <--PWM--> TB6612FNG <--> 4x DC Motors
                                          ▲
                                          │ CSI
                                      Camera (OV5647)
```

</details>

<details>
<summary><strong><ins>Roadmap</ins></strong></summary>


<details><summary>Hardware: Data Exchange</summary>


#### Arduino <--> Motor Driver <--> Wheels

- [x] Verify TB6612 (motor driver) wiring on breadboard
- [x] Connect motor driver to Arduino Uno R3 using protoshield  
  *(need copper wire, soldering iron stand, solder sucker, cleaning sponge)*
- [ ] Attach Uno to chassis, and connect DC motors to Uno through protoshield
- [ ] Attach battery pack to chassis, and connect it to DC motors (as their power source) through motor driver
- [ ] Verify that Uno is able to control all 4 wheels while attached to chassis

---

#### Raspberry Pi <--> Arduino

- [ ] Test UART communication only from Raspberry Pi 3B+ to Arduino Uno R3
- [ ] Using a breadboard, test UART communication from the Uno to Pi with a level shifter from 5V to 3.3V
- [ ] Solder level shifter to protoshield and set bi-directional UART communication through protoshield
- [ ] Verify communication between Pi and Uno
- [ ] Create script for Uno to receive commands through Serial and write to motors
- [ ] Verify that Pi is able to control all 4 wheels using Uno as intermediary

---

#### Desktop <--> Raspberry Pi

- [ ] Figure out ROS2 communication between desktop and Raspberry Pi 3B+ over Wi-Fi  
  *(possibly need a router)*
- [ ] Create bridge node on Pi for translating ROS2 Twist messages to workable PWM values that can be sent to Arduino
- [ ] Verify that Pi is able to subscribe to topics, receive Twist messages, and use it to control the wheels

---

#### Desktop <--> Raspberry Pi <--> Arduino <--> Motor Driver <--> Wheels

- [ ] Verify full communication architecture with [Hand Controller](https://github.com/hcr-vvatel/hand_controller)

---

#### Camera <--> Raspberry Pi <--> Desktop

- [ ] Figure out how to send video feed from onboard camera to desktop


</details>


<details><summary>Software: Perception + Navigation</summary>


#### Perception Stack

- [ ] Research SLAM and find ROS2 implementations

---

#### Navigation Stack

- [ ] Figure out ROS2 Nav2 package


</details>


</details>


<details>
<summary><strong><ins>Timeline</ins></strong></summary>

<details> <summary><strong>8/16/26</strong> - Successfully connected TB6612 to Arduino through protoshield </summary><br>

<p>Gathered the proper equipment including a new soldering iron, stand, a soldering tip cleaner, and copper wire. </p>
<img width="300" height="300" alt="20260816_213656" src="https://github.com/user-attachments/assets/f85936cc-1841-45b1-aafb-b38fc9b71ccd" />
<p><b>Figure 8.16-1.</b> New protoshield held by recently acquired soldering stand</p>

<p>With all of this stuff, my second attempt at soldering the TB6612 onto the protoshield and then connecting it to the Arduino's pins was much cleaner. </p>
<img width="300" height="300" alt="20260816_213705" src="https://github.com/user-attachments/assets/99bc6218-a832-4ad2-83af-b97149881f7b" />
<p><b>Figure 8.16-2.</b> TB6612 - Arduino wiring using solder to connect copper wire at two points</p>

<p>I connected the protoshield and Arduino together and confirmed the TB6612FNG was working!</p>
<img width="300" height="300" alt="20260816_223415" src="https://github.com/user-attachments/assets/f09eab62-9928-450d-bb55-1cd4fab487a8" />
<p><b>Figure 8.16-3.</b> Protoshield on top of Arduino R3 </p>

<p>Now comes the hard part, actually wiring the motors and power supply to the protoshield. My initial, brute force plan is to just connect pairs of holes on the protoshield together on the bottom with copper wire, then use each pair of holes, to connect pins on the Arduino, pins on the motor driver, and wires from the motors and battery pack together.</p>

</details>

---

<details> <summary><strong>8/2/26</strong> - Attempted to permanently set wiring between TB6612 and Arduino using a protoshield </summary><br>

<p>Bought some <a href="https://a.co/d/0bSkkdKM">protoshields</a> for the Arduino Uno R3, but they were physically incapable of seating on top of the Uno due to the heights of the ethernet port and power jack. To fix this, I used V-scoring to cut off an unnecessary part of the shield (<b>Figure 8.2-1</b>).</p>

<img width="300" height="300" alt="20260802_121438" src="https://github.com/user-attachments/assets/169c2e2a-2213-468d-b7d5-6f155d1b600b" />
<p><b>Figure 8.2-1.</b> Results of cutting protoshield; the red shield on top shows the original length.</p>

<p>After that, I soldered header pins onto the protoshield so that I could plug it into the female pins on the Arduino (<b>Figure 8.2-2</b>). The protoshield has a partner hole directly next to each solder joint, giving access to the underlying Arduino pin.</p>

<img width="300" height="300" alt="20260802_132939" src="https://github.com/user-attachments/assets/6d25d373-3a61-41bd-9053-e8e1016c2ef5" />
<p><b>Figure 8.2-2.</b> Protoshield attached by header pins to the Arduino; the holes near each solder joint allow access to the actual Arduino pins.</p>

<p><b>Notably:</b> For some of the pins, a bit of solder fell and clogged their partnered hole due to lack of experience. In the future, I should obtain a solder sucker to fix mistakes like this.</p>

<p>I then soldered the motor driver onto the protoshield and attempted to use lines of solder to replicate the wiring between the motor driver and the Arduino. On the surface, solder connects the partner holes to holes near the motor driver; underneath, solder connects the holes near the motor driver to the motor driver's pins (<b>Figure 8.2-3</b>).</p>

<img width="300" height="300" alt="20260802_210347" src="https://github.com/user-attachments/assets/58767552-1775-463c-8933-3c89f7fc059d" />
<p><b>Figure 8.2-3.</b> Motor driver soldered onto protoshield; the raised lines of solder are used as wire to bridge the motor driver and Arduino.</p>

<p><b>Notably:</b> Lacking equipment such as a sponge to clean the soldering iron and a stand to hold it while hot made this very difficult and time-consuming. Without being able to clean the iron of buildup, it was hard to make tiny, precise connections without accidentally creating a short circuit. In the future, I should obtain a soldering iron stand. Additionally, using solder as both the wire and the connector is difficult — in the future, I should obtain and use copper wire instead.</p>

<p>Ultimately, this attempt failed. I'll get the proper equipment and supplies before trying again.</p>

</details>

---

<details> <summary><strong>7/31/26</strong> - Verified TB6612 (Motor Driver) control logic on breadboard</summary><br>

<p>Bought a <a href="https://a.co/d/0d0911Pa">TB6612 Motor Driver</a> and soldered the header pins onto it. I tested the wiring between the Arduino, the motor driver, and one of the car's motors using a breadboard. Then, I wrote a <a href="arduino/tests/motor_driver_test/motor_driver_test.ino">script</a> to test the motor driver's control logic (<b>Figure 7.31-1</b>).</p>

https://github.com/user-attachments/assets/8c097552-bbd2-4168-9c4e-e303f9cf0ce9
<p><b>Figure 7.31-1.</b> Motor driver control logic test — STBY, AIN1/AIN2, and PWMA signals verified with a multimeter before connecting battery power.</p>

<p><b>Issue:</b> After wiring in battery power, STBY unexpectedly read 0V. STBY needs to constantly be set to HIGH, otherwise the motor driver operates in sleep mode. Isolated the fault via systematic voltage tracing using a multimeter and found a cold solder joint on the STBY header pin. Reheating the joint solved the issue.</p>

</details>

---

<details> <summary><strong>7/26/26</strong> - Redesigned robot control architecture</summary><br>

<p>
  Initially thought to establish communication with a host computer running ROS2 to the onboard Arduino using an ESP32-S3 microcontroller (included with the kit) as the intermediary. Found that the I/O Expansion shield (placed on top of the Arduino) and the ESP32 were too customized/undocumented to extend for this project. Decided to scrap both parts, and instead use a different microcontroller as the intermediary.
</p>
<p><b>Notably:</b> Because of this replacement, I lost access to the motor driver (TB6612FNG) attached to the I/O Expansion Shield, so I would need to wire in one on my own.</p>
<p>
  For the intermediary, I chose to use the Raspberry Pi Model 3 B+ (<b>Figure 7.26-1</b>). This Pi was chosen mainly due to budget constraints. Since the project will initially run most computations through my desktop, the Pi only needs enough power to broadcast images over Wi-Fi, run ROS2 to receive commands, and translate those commands into workable Serial that can be written to the motors. Though a stronger Pi could run the computations itself, it is too expensive at the moment. The final structure will look like:
</p>
<p>Host Computer &lt;---ROS2 Messages---&gt; RPi 3B+ &lt;----Serial----&gt; Arduino</p>

<img width="200" height="200" alt="Raspberry Pi 3B+" src="https://github.com/user-attachments/assets/7fdf3846-9356-4677-be20-b20eb48023ae" />
<p><b>Figure 7.26-1.</b> Raspberry Pi Model 3 B+, chosen as the desktop to Arduino intermediary.</p>

</details>

---

<details> <summary><strong>7/1/26</strong> - Built smart car from kit</summary><br>

<p>Initially decided to purchase a cheap autonomous vehicle kit (<b>Figure 7.1-1</b>). This would've allowed me to focus on writing the software for the project and not have to worry about custom-built hardware.</p>

<img width="200" height="200" alt="Elegoo Smart Car" src="https://github.com/user-attachments/assets/0bfb81bb-cc9d-4f42-a743-23ac3eee5569" />
<p><b>Figure 7.1-1.</b> ELEGOO Smart Robot Car Kit V4.0, as originally assembled.</p>

</details>


</details>
  
  

