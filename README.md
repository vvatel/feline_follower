# Feline Follower (Autonomous Pet-Tracking Robot)
Real-time visual tracking and SLAM-based navigation to follow fast, erratic motion

## Progress Timeline

  <details> <summary><strong>7/26/26</strong> - Redesigned Robot Control Architecture</summary>
    Attempted to setup communication between personal computer running ROS2 and Arduino R3 utilizing included ESP32-S3 microcontroller in the kit as the intermediary but found that the kit's I/O expansion shield (attached to the Arduino) and the ESP32 itself were too customized/undocumented to extend their use past what was given with the kit. Instead, decided to remove both the I/O Expansion Shield and the ESP32, and instead use a Raspberry Pi as the intermediary. Arduino ⟺ Raspberry Pi ⟺ ROS2
  </details>
  
  <details> <summary><strong>7/1/26</strong> - Finished Building Smart Car from Kit</summary>
    Initially decided to purchase a [cheap autonomous vehicle kit](https://us.elegoo.com/products/elegoo-smart-robot-car-kit-v-4-0) to focus on the software side of the project
  </details>
  
  
  

